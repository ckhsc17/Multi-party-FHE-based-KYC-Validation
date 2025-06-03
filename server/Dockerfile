FROM python:3.9-slim

# 建立工作目錄
WORKDIR /server

# 複製依賴與程式碼
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 8080

# 預設執行 FastAPI 應用
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8080"]
