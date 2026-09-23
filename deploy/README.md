# Docker Compose 接入示例

这里的文件用于把本模块接入已有 Odoo 8 Compose 栈，不包含数据库、反向代理或任何业务服务定义。

## 用法

设置三个宿主机绝对路径：

```bash
export ODOO_ADDONS_UNION_HOST_PATH=/srv/odoo/runtime/addons-union
export ODOO_BASE_ADDONS_HOST_PATH=/srv/odoo/current/addons
export RESPONSIVE_ADDONS_HOST_PATH=/srv/tdm-web-responsive-v8/current/addons
```

建立只读 addons 联合目录：

```bash
./deploy/rebuild_addons_union.sh \
  "$ODOO_BASE_ADDONS_HOST_PATH" \
  "$RESPONSIVE_ADDONS_HOST_PATH" \
  "$ODOO_ADDONS_UNION_HOST_PATH"
```

预览 Compose 合并结果，再只重建 Odoo 服务：

```bash
docker compose -f /path/to/existing-compose.yaml \
  -f deploy/compose.override.yaml config

docker compose -f /path/to/existing-compose.yaml \
  -f deploy/compose.override.yaml up -d --no-deps odoo
```

联合目录中的符号链接指向容器内的 `/mnt/base-addons` 和 `/mnt/responsive-addons`。三个宿主机路径均以只读方式挂载；基础 Compose 文件、数据库和数据卷不会被本项目改写。

切换前请确认合并配置没有改变数据库服务、网络、端口、镜像或数据卷。发布和回滚只重建 Odoo 服务，不执行 `down`，也不删除卷。
