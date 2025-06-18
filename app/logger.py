# app/logger.py
import csv
from datetime import datetime

async def log_attack(request, attack_type):
    with open("dashboard/logs/attacks.csv", "a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([
            datetime.utcnow().isoformat(),
            str(request.client.host),
            str(request.url),
            attack_type
        ])
