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

### docker compose
```bash
docker-compose up --build
```

## 性能追踪
[prometheus_flask_exporter](https://github.com/rycus86/prometheus_flask_exporter)

