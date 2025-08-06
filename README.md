# fa-flask
> 一个简单的flask接口框架

## Get Start
1. 安装pdm（如果没有安装）：
```bash
```

2. 安装依赖
```bash
pdm install
```

3. 启动服务
> 启动服务，默认 http://127.0.0.1:5000
```bash
pdm run serve
```

## Docker
# 构建镜像
```bash
docker build -t flask-pdm-app .
```

# 运行容器
```bash
docker run -p 5000:5000 flask-pdm-app
```

### docker compose启动全部服务
```bash
docker-compose up --build
```

- Prometheus UI → http://localhost:9090
- Grafana UI → http://localhost:3000 （默认账户：admin / admin）

## 性能追踪
[prometheus_flask_exporter](https://github.com/rycus86/prometheus_flask_exporter)

### 在 Grafana 添加数据源和仪表盘
#### 添加数据源：
1. 登录 Grafana → Settings > Data Sources
2. 添加 Prometheus
3. URL 填写：http://prometheus:9090

#### 创建仪表盘：
可以创建如下面板：

| 面板名称   | 指标名称                                        |
|--------|---------------------------------------------|
| 请求总数   | flask_http_request_total                    |
| 平均响应时间 | flask_http_request_duration_seconds_average |
| 每秒请求数  | rate(flask_http_request_total[1m])          |
| 错误率    | rate(flask_http_request_errors_total[1m])   |

或者导入社区 Dashboard（ID： 4701 或 11074 等）。
