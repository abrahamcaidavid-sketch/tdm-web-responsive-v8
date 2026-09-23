#!/bin/sh
set -eu

if test "$#" -ne 3; then
    echo "usage: $0 BASE_ADDONS RESPONSIVE_ADDONS UNION_ROOT" >&2
    exit 64
fi

base_addons=$1
responsive_addons=$2
union_root=$3

test -d "$base_addons"
test -d "$responsive_addons/tdm_web_responsive_v8"

runtime_root=$(dirname "$union_root")
mkdir -p "$runtime_root"
staged=$(mktemp -d "$runtime_root/addons-union.tmp.XXXXXX")
cleanup() {
    rm -rf "$staged"
}
trap cleanup EXIT HUP INT TERM

for module_path in "$base_addons"/*; do
    test -d "$module_path" || continue
    module_name=$(basename "$module_path")
    ln -s "/mnt/base-addons/$module_name" "$staged/$module_name"
done

ln -s /mnt/responsive-addons/tdm_web_responsive_v8 \
    "$staged/tdm_web_responsive_v8"
chmod 0755 "$staged"

previous="$runtime_root/addons-union.previous"
rm -rf "$previous"
if test -e "$union_root"; then
    mv "$union_root" "$previous"
fi
mv "$staged" "$union_root"
trap - EXIT HUP INT TERM
