# TDM Web Responsive for Odoo 8

让经典的 Odoo 8 后台在手机和平板浏览器上更易用。

`tdm_web_responsive_v8` 是一个独立安装的响应式 Web Client 扩展。它为窄屏加入抽屉式菜单，改善表单、看板、弹窗、页签与状态栏布局，并保留复杂列表的横向滚动能力。模块不修改 Odoo 官方核心、不改变业务表，也不替代现有业务模块。

## 主要特性

- 支持 360px、390px、768px 等常见移动端宽度。
- 窄屏左侧菜单可通过按钮、遮罩或 `Esc` 键关闭。
- 表单、看板、弹窗、页签和状态栏适应可用宽度。
- 复杂列表保留横向滚动，避免字段被强行压缩。
- 大于 991px 时保持 Odoo 8 原有桌面布局。
- 仅依赖官方 `web` 模块，作为独立 Custom Addon 安装。

## 兼容范围

- Odoo 8.0 的标准 `web` 客户端。
- 现代 Android Chrome、iOS Safari 及同内核企业浏览器。
- 深度改写 `web.webclient_bootstrap` 或 `.oe_leftbar` 的第三方主题可能冲突，部署前应在测试数据库验证。

本项目参考了 [OCA/web](https://github.com/OCA/web) 中 `web_responsive` 的设计方向，但针对 Odoo 8 的 `openerp.<module>`、QWeb 和旧版 DOM 结构独立实现，没有复制较新 Odoo 版本的不兼容 API。

## 安装

1. 从 [Releases](../../releases) 下载 `tdm_web_responsive_v8-<版本>.zip` 并校验同名 `.sha256` 文件。
2. 解压后把完整的 `tdm_web_responsive_v8` 目录放入独立的 Custom Addons 路径。
3. 确认该路径已加入 `addons_path`，更新模块列表并安装 **TDM Web Responsive for Odoo 8**。
4. 清理浏览器缓存，在手机和桌面浏览器完成关键业务回归。

命令行安装示例：

```bash
./openerp-server -c /path/to/odoo.conf -d TEST_DB \
  -i tdm_web_responsive_v8 --stop-after-init
```

完整的上线、验收和回滚清单见 [DEPLOYMENT.md](DEPLOYMENT.md)。Docker Compose 接入示例见 [deploy/README.md](deploy/README.md)。

## 开发与验证

```bash
python -m unittest discover -s addons/tdm_web_responsive_v8/tests -p "test_*.py" -v
python scripts/build_release.py
```

第二条命令会生成可复现的模块 ZIP 和 SHA-256 校验文件。提交和 Pull Request 会由 GitHub Actions 自动验证。

## 一键发布

仓库维护者在 GitHub 的 **Actions → Release → Run workflow** 中点击运行即可。固定流程会：

1. 校验 `VERSION`、模块清单、XML 和静态资源；
2. 运行测试并构建可复现 ZIP；
3. 生成 SHA-256 校验文件；
4. 创建 `v<版本>` 标签和 GitHub Release，并附上两个发布文件。

发布下一版前，在同一个提交中更新根目录的 [VERSION](VERSION) 和模块清单 `addons/tdm_web_responsive_v8/__openerp__.py` 中的 `version`；工作流会核对两者一致，并用 `VERSION` 生成标签。已存在的版本标签不会被覆盖。

## 贡献

欢迎提交 Issue 和 Pull Request。请先阅读 [CONTRIBUTING.md](CONTRIBUTING.md)；安全问题请按 [SECURITY.md](SECURITY.md) 中的方式处理。

## 许可证

[LGPL-3.0-or-later](LICENSE.md)。
