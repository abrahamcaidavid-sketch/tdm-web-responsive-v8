# Contributing

感谢你帮助改进 TDM Web Responsive for Odoo 8。

## 提交变更

1. 从 `main` 创建短期分支。
2. 保持模块只依赖 Odoo 8 官方 `web`，不要修改或复制 Odoo 核心文件。
3. 对行为变化补充静态测试，并在 360px、390px、768px 和桌面宽度完成浏览器验证。
4. 运行：

   ```bash
   python -m unittest discover -s addons/tdm_web_responsive_v8/tests -p "test_*.py" -v
   python scripts/build_release.py
   ```

5. 提交 Pull Request，说明问题、实现方式、验证结果和兼容性影响。

版本号遵循 Odoo 常用的 `<Odoo主版本>.<功能版本>` 形式，以根目录 `VERSION` 与 `__openerp__.py` 中的版本一致为准。
