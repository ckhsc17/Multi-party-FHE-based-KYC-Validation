# model_train.py
from concrete.ml.sklearn import LogisticRegression
import numpy as np
import time

# 模擬資料（UID hash 對應風險等級）
X_train = np.random.randint(0, 2**16, size=(300, 1)).astype(np.float32)
y_train = X_train[:, 0].astype(int) % 3  # 三分類：低中高風險（0/1/2）

# 建立與編譯模型
model = LogisticRegression()
model.fit(X_train, y_train)

print("⏳ 編譯 FHE 模型中...")
start_time = time.time()
model.compile(X_train)
print(f"✅ 編譯完成，耗時 {time.time() - start_time:.2f} 秒")

# 儲存模型（會包含 FHE artifact）
model.save("fhe_model")
print("✅ FHE 模型已儲存")
