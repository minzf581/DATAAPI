# DataAPI

一个基于FastAPI的数据管理API服务，支持数据上传、加密和存储功能。

## 功能特点

- 文件上传和管理
- 自动数据加密
- Google Cloud Storage集成
- PostgreSQL数据库支持
- 异步操作支持
- 完整的测试覆盖

## 技术栈

- Python 3.13+
- FastAPI
- SQLAlchemy (异步)
- PostgreSQL
- Google Cloud Storage
- pytest
- cryptography

## 安装

1. 克隆仓库：
```bash
git clone https://github.com/minzf581/DataAPI.git
cd DataAPI
```

2. 创建虚拟环境：
```bash
python -m venv venv
source venv/bin/activate  # Linux/Mac
# 或
.\venv\Scripts\activate  # Windows
```

3. 安装依赖：
```bash
pip install -r requirements.txt
```

4. 配置环境变量：
```bash
cp .env.example .env
# 编辑 .env 文件，填入必要的配置信息
```

## 配置

在 `.env` 文件中配置以下环境变量：

- `DATABASE_URL`: PostgreSQL数据库连接URL
- `GOOGLE_CLOUD_PROJECT`: Google Cloud项目ID
- `GOOGLE_APPLICATION_CREDENTIALS`: Google Cloud认证文件路径
- `BUCKET_NAME`: Google Cloud Storage存储桶名称

## 运行

1. 启动服务：
```bash
uvicorn app.main:app --reload
```

2. 访问API文档：
- Swagger UI: http://localhost:8000/docs
- ReDoc: http://localhost:8000/redoc

## 测试

运行测试：
```bash
pytest -v
```

## API文档

### 主要端点

- `GET /health`: 健康检查
- `POST /api/data/upload`: 上传数据
  - 支持文件上传
  - 自动加密
  - 存储到GCS
  - 返回数据集ID和存储路径

## 贡献

欢迎提交Issue和Pull Request！

## 许可证

MIT License 