#!/usr/bin/env python3
"""Build a deterministic Odoo module ZIP and its SHA-256 checksum."""

from __future__ import annotations

import argparse
import ast
import hashlib
from pathlib import Path
import re
import zipfile


ROOT = Path(__file__).resolve().parents[1]
MODULE_NAME = "tdm_web_responsive_v8"
MODULE_ROOT = ROOT / "addons" / MODULE_NAME
VERSION_PATTERN = re.compile(r"^8\.0\.\d+\.\d+\.\d+$")
ZIP_TIMESTAMP = (2026, 1, 1, 0, 0, 0)


def read_version() -> str:
    version = (ROOT / "VERSION").read_text(encoding="utf-8").strip()
    if not VERSION_PATTERN.fullmatch(version):
        raise SystemExit("VERSION must match 8.0.X.Y.Z")

    manifest = ast.literal_eval(
        (MODULE_ROOT / "__openerp__.py").read_text(encoding="utf-8")
    )
    if manifest.get("version") != version:
        raise SystemExit("VERSION and __openerp__.py version do not match")
    if manifest.get("license") != "LGPL-3":
        raise SystemExit("__openerp__.py must declare LGPL-3")
    return version


def iter_module_files():
    for path in sorted(MODULE_ROOT.rglob("*")):
        if not path.is_file():
            continue
        if "__pycache__" in path.parts or path.suffix in {".pyc", ".pyo"}:
            continue
        yield path


def write_zip(destination: Path) -> None:
    with zipfile.ZipFile(destination, "w", compression=zipfile.ZIP_STORED) as archive:
        for path in iter_module_files():
            relative = path.relative_to(MODULE_ROOT)
            info = zipfile.ZipInfo(
                (Path(MODULE_NAME) / relative).as_posix(), ZIP_TIMESTAMP
            )
            info.compress_type = zipfile.ZIP_STORED
            info.create_system = 3
            info.external_attr = 0o100644 << 16
            archive.writestr(info, path.read_bytes())


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--output-dir", type=Path, default=ROOT / "dist", help="output directory"
    )
    parser.add_argument(
        "--expected-version", help="fail unless this matches the repository version"
    )
    args = parser.parse_args()

    version = read_version()
    if args.expected_version and args.expected_version != version:
        raise SystemExit(
            "requested version %s does not match VERSION %s"
            % (args.expected_version, version)
        )

    args.output_dir.mkdir(parents=True, exist_ok=True)
    archive_path = args.output_dir / ("%s-%s.zip" % (MODULE_NAME, version))
    write_zip(archive_path)

    digest = hashlib.sha256(archive_path.read_bytes()).hexdigest()
    checksum_path = archive_path.with_suffix(archive_path.suffix + ".sha256")
    checksum_path.write_text(
        "%s  %s\n" % (digest, archive_path.name), encoding="ascii", newline="\n"
    )
    print(archive_path)
    print(checksum_path)
    print("sha256=%s" % digest)


if __name__ == "__main__":
    main()
