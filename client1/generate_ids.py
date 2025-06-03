import random

def generate_ids(filename="client1/client1.txt", count=10):
    with open(filename, "w") as f:
        for _ in range(count):
            uid = random.randint(1000, 9999)  # 模擬 4 位數 UID
            f.write(f"{uid}\n")

if __name__ == "__main__":
    generate_ids()
    print("✅ client1.txt 已產生完成")
