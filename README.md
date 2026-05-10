# 车辆大屏可视化项目说明

本文档概述整个「车辆大屏可视化」工程的结构、技术栈与使用方式。爬虫脚本位于 **`spiderMan/`** 子目录；本说明文件位于**项目根目录**，与 `spiderMan` 同级。

---

## 一、项目做什么

本项目围绕**懂车帝**等来源的**汽车排行与参数数据**，完成三件事：

1. **数据采集**：从网站接口与详情页抓取品牌、车系、销量、价格区间、车型、能源类型、上市时间、保修等信息。  
2. **数据存储**：通过 Django 将数据写入 **MySQL**（库名在配置中为 `carData`，表 `carInfo` 等）。  
3. **数据展示**：使用 **Vue 2** 大屏模板（`@jiaminghi/data-view` + **ECharts**）做可视化，页面标题为「懂车帝-长沙市汽车信息」，通过接口拉取后端统计结果。

---

## 二、目录结构（核心部分）

| 路径 | 说明 |
|------|------|
| `manage.py`、`车辆大屏可视化/` | Django 工程入口与配置（`settings.py`、`urls.py` 等） |
| `myApp/` | 业务应用：`models.py`（车辆 `carInfo`、用户 `User`）、`views.py`、各图表数据 `utils/*.py` |
| `spiderMan/` | 爬虫：`spiders.py`、`page.txt`（分页偏移记录），运行后可能在该目录生成 `temp.csv` |
| `big-screen-vue-datav-master/` | 前端大屏：Vue CLI 项目，axios 默认请求 `http://127.0.0.1:8000/` |
| `requirementsDjango.txt` | Python / Django 侧依赖清单（含 `requests`、`lxml`、`pandas`、Django、PyMySQL 等） |
| 根目录 `package.json` | 仅声明了 `axios`（大屏主要依赖在子项目 `package.json` 中） |

---

## 三、技术栈摘要

- **后端**：Django（配置中标注 6.x 生成，依赖文件含 Django 4.2+），**django-cors-headers** 开启跨域，便于本地前后端联调。  
- **数据库**：MySQL，连接信息在 `车辆大屏可视化/settings.py` 的 `DATABASES` 中，需自行创建数据库并执行迁移。  
- **前端**：Vue 2、Vue Router、Vuex、ECharts 4、`@jiaminghi/data-view`、`vue-awesome`。  
- **爬虫**：`requests` + `lxml`，可选经 CSV 清洗后 `carInfo.objects.create(...)` 入库。

---

## 四、环境与运行顺序

### 1. MySQL

- 创建与 `settings.py` 中 `NAME` 一致的数据库（如 `carData`）。  
- 在 `settings.py` 中填写正确的 `USER`、`PASSWORD`、`HOST`、`PORT`（勿将生产密码提交到公开仓库）。  
- 在项目根目录执行：`python manage.py migrate`  

### 2. Django 后端

```bash
# 建议在项目根目录「车辆大屏可视化」下
pip install -r requirementsDjango.txt
python manage.py runserver 0.0.0.0:8000
```

接口前缀为：`http://127.0.0.1:8000/myApp/`，例如：

- `GET /myApp/center/` — 中间区域汇总与能源占比等  
- `GET /myApp/centerleft/`、`/myApp/bottomleft/`、`/myApp/centerright/`、`/myApp/bottomright/` 等 — 各模块图表数据  
- `GET /myApp/centermostright/<energyType>/` — `energyType` 为路径中的整数，用于区分燃油 / 新能源等展示逻辑  

### 3. 爬虫（`spiderMan/`）

- 运行前需保证 **Django 能加载到项目**（一般在**项目根目录**执行，或将根目录加入 `PYTHONPATH`），且 **MySQL 与模型已就绪**。  
- `spiderMan/page.txt` 记录当前爬取偏移；`init()` 会在当前工作目录下初始化 `temp.csv` 表头（若从 `spiderMan` 内运行，文件通常生成在该目录）。  
- 懂车帝接口含签名、Cookie 等反爬参数，**易过期**；若请求失败需按最新浏览器抓包更新 `spiders.py` 中的 URL、Header、Cookie 等。  
- 目标站点数据与规则版权归原网站所有，请遵守其服务条款与法律法规，**仅建议用于学习研究**。

### 4. 前端大屏

```bash
cd big-screen-vue-datav-master
npm install
npm run serve
```

若后端地址不是 `127.0.0.1:8000`，请修改 `big-screen-vue-datav-master/src/api/index.js` 中的 `baseURL`。

---

## 五、数据模型（`myApp.models`）简要

- **`carInfo`**：品牌、车名、图片链接、销量、价格、厂商、排名、车型、能源类型、上市时间、保修时间、创建时间等。  
- **`User`**：用户名、密码、创建时间（如用于后续扩展登录等）。

大屏各接口在 `myApp/views.py` 中聚合 `utils` 下脚本，对 `carInfo` 等表做统计后返回 JSON。

---

## 六、注意事项

1. **安全**：`DEBUG = True`、默认 `SECRET_KEY`、数据库口令等仅适用于本地开发；上线前必须按 Django 部署规范加固。  
2. **爬虫稳定性**：第三方页面 XPath、接口字段可能变更，需随站点更新维护。  
3. **依赖版本**：前端为 Vue CLI 4 + Vue 2，建议使用与 `package.json` 相近的 Node 版本，避免构建报错。

---

## 七、文档位置

本说明文件路径：**项目根目录下的 `README.md`**（与 `spiderMan/` 文件夹同级）。

如需补充接口字段说明或部署截图，可在此文件后续章节自行追加。
