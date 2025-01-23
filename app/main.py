from fastapi import FastAPI, File, UploadFile, Form, HTTPException, Depends, status
from sqlalchemy.ext.asyncio import AsyncSession
import uuid
import logging
from app.database.database import get_db
from app.storage.client import get_storage_client
from app.models.data import Dataset
from app.utils.encryption import generate_encryption_key, encrypt_data

app = FastAPI()
logger = logging.getLogger(__name__)

@app.get("/health")
async def health_check():
    """健康检查端点"""
    return {"status": "healthy"}

@app.post("/api/data/upload")
async def upload_data(
    data_file: UploadFile = File(...),
    data_description: str = Form(...),
    privacy_algorithm: str = Form(...),
    access_policy: str = Form(...),
    db: AsyncSession = Depends(get_db),
    storage_client = Depends(get_storage_client)
):
    try:
        logger.info(f"开始处理数据上传请求: {data_file.filename}")
        
        # 生成唯一标识符
        dataset_id = str(uuid.uuid4())
        
        # 生成加密密钥
        logger.info("正在生成加密密钥...")
        encryption_key = generate_encryption_key()
        
        # 读取和加密数据
        logger.info("正在加密数据...")
        file_content = await data_file.read()
        encrypted_data = encrypt_data(file_content, encryption_key)
        
        # 构建存储路径
        storage_path = f"data/{dataset_id}/{data_file.filename}"
        logger.info(f"文件将被保存到: {storage_path}")
        
        # 上传到存储
        logger.info("正在上传加密数据到存储...")
        bucket = storage_client.bucket("your-bucket-name")
        blob = bucket.blob(storage_path)
        blob.upload_from_string(encrypted_data)
        logger.info("数据上传到存储成功")
        
        # 创建数据集记录
        logger.info("创建数据集记录...")
        dataset = Dataset(
            id=dataset_id,
            file_name=data_file.filename,
            storage_path=storage_path,
            description=data_description,
            privacy_algorithm=privacy_algorithm,
            access_policy=access_policy,
            encryption_key=encryption_key
        )
        
        # 保存到数据库
        logger.info("添加数据集到数据库会话...")
        db.add(dataset)
        await db.commit()
        await db.refresh(dataset)
        
        return {
            "dataset_id": dataset.id,
            "storage_path": dataset.storage_path
        }
        
    except Exception as e:
        logger.error(f"未预期的错误: {str(e)}")
        try:
            await db.rollback()
        except:
            pass
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=str(e)
        ) 