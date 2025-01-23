from datetime import datetime, timezone
from sqlalchemy import Column, String, DateTime, JSON
from sqlalchemy.orm import declarative_base

Base = declarative_base()

class Dataset(Base):
    __tablename__ = "datasets"

    id = Column(String, primary_key=True, index=True)
    file_name = Column(String, nullable=False)
    storage_path = Column(String, nullable=False)  # 在Google Cloud Storage中的路径
    description = Column(String, nullable=False)
    privacy_algorithm = Column(String, nullable=False)
    access_policy = Column(String, nullable=False)
    encryption_key = Column(String, nullable=False)  # 存储加密密钥
    created_at = Column(DateTime(timezone=True), nullable=False)
    updated_at = Column(DateTime(timezone=True), nullable=False)

    def __init__(self, **kwargs):
        current_time = datetime.now(timezone.utc)
        kwargs.setdefault('created_at', current_time)
        kwargs.setdefault('updated_at', current_time)
        super().__init__(**kwargs) 