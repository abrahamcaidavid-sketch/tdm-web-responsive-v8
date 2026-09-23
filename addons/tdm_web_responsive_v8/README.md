# TDM Web Responsive for Odoo 8

`tdm_web_responsive_v8` 是一个独立的 Odoo 8 后台手机浏览器适配模块，不修改
Odoo 核心代码，也不创建或变更业务数据表。

## 功能

- 为 Odoo 8 WebClient 增加移动端 viewport。
- 在窄屏下把左侧二级菜单改为可开关的抽屉菜单。
- 表单、看板、对话框、页签和状态栏适应手机宽度。
- 列表与复杂表格保留横向滚动，避免强行压缩后字段不可读。
- 桌面端宽度大于 991px 时保持原有布局。

## 兼容范围

- Odoo 8.0 社区版/企业定制版的标准 `web` 客户端。
- 现代 Android Chrome、iOS Safari 及同内核企业浏览器。
- 与深度改写 `web.webclient_bootstrap` 或 `.oe_leftbar` 的第三方后台主题可能冲突，
  必须先在测试库验证。

本模块参考了 OCA `web_responsive` 的“移动端菜单 + 响应式布局”设计方向，但代码
按 Odoo 8 的 `openerp.<module>`、QWeb 和 DOM 结构重新实现，没有复制 Odoo 9+ 的
不兼容 JavaScript API。

## 安装

详细的上线步骤、验收清单与回滚方式见 [DEPLOYMENT.md](DEPLOYMENT.md)。

## 许可证

LGPL-3.0-or-later。

