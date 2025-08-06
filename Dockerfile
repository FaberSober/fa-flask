FROM python:3.11-slim

# 安装PDM
RUN pip install --no-cache-dir pdm

# 设置工作目录
WORKDIR /app

# 复制项目文件
COPY . /app

# 安装依赖
RUN pdm install --prod

# 暴露端口
EXPOSE 5000

# 启动服务
CMD ["pdm", "run", "serve"]
