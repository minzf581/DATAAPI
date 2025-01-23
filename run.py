import uvicorn
from dotenv import load_dotenv
import os

if __name__ == "__main__":
    # 加载环境变量
    load_dotenv()
    
    # 获取配置
    host = os.getenv("API_HOST", "0.0.0.0")
    port = int(os.getenv("API_PORT", "8000"))
    
    # 启动应用
    uvicorn.run(
        "app.main:app",
        host=host,
        port=port,
        reload=True  # 开发模式下启用热重载
    ) 