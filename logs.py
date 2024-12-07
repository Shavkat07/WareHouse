import json
from datetime import datetime

# Loglarni JSON faylga saqlash
def save_log(log, filename="logs.json"):
    try:
        # Eski loglarni o'qish
        with open(filename, "r") as file:
            data = json.load(file)
    except FileNotFoundError:
        data = []  # Fayl mavjud bo'lmasa, bo'sh ro'yxat

    # Yangi logni qo'shish
    data.append(log)

    # JSON faylga yozish
    with open(filename, "w") as file:
        json.dump(data, file, indent=4)
    print("Log saqlandi!")

# Loglarni JSON fayldan o'qish
def get_logs(start_time=None, end_time=None, filename="logs.json"):
    try:
        with open(filename, "r") as file:
            logs = json.load(file)
    except FileNotFoundError:
        return []

    # Vaqt oralig'ini filtrlash
    if start_time and end_time:
        filtered_logs = [
            log for log in logs
            if "timestamp" in log and start_time <= datetime.fromisoformat(log["timestamp"]) <= end_time
        ]
        return filtered_logs

    return logs
