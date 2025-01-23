from pydantic import BaseModel
from datetime import datetime
from typing import Dict, Optional

class DataUploadRequest(BaseModel):
    data_description: str
    privacy_algorithm: str
    access_policy: str

class DatasetResponse(BaseModel):
    id: int
    description: str
    privacy_algorithm: str
    access_policy: str
    file_path: str
    encryption_metadata: Dict
    created_at: datetime
    updated_at: datetime

    class Config:
        from_attributes = True

class DataUploadResponse(BaseModel):
    dataset_id: int
    file_path: str 