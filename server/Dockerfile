FROM python:3.9-slim

# 安裝必要套件
RUN apt-get update && apt-get install -y build-essential

# 建立工作目錄
WORKDIR /app

# 複製依賴與程式碼
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

# 預設執行 FastAPI 應用
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8080"]
