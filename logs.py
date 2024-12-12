import json
from datetime import datetime
from data import save_data_to_file, load_data_from_file

# Loglarni JSON faylga saqlash
def save_log(log):
    save_data_to_file(file_name="logs", data=log)
    print("Log saqlandi!")

# Loglarni JSON fayldan o'qish
def get_logs(start_time=None, end_time=None,):
    logs = load_data_from_file(file_name='logs', param_key='all')
    # Vaqt oralig'ini filtrlash
    if start_time and end_time:
        filtered_logs = [
            log for log in logs
            if "timestamp" in log and start_time <= datetime.fromisoformat(log["timestamp"]) <= end_time
        ]
        return filtered_logs
    print(logs)
    return logs
