# src/utils.py
import datetime

def scrivi_log(messaggio):
    with open("data/hulara.log", "a") as f:
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        f.write(f"[{timestamp}] {messaggio}\n")
