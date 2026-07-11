# codes/utils/data_exporter.py
import json

def salva_specs(nome_modello, cpu, ram, storage):
    data = {
        "modello": nome_modello,
        "cpu": cpu,
        "ram": ram,
        "storage": storage
    }
    file_path = f"data/{nome_modello.replace(' ', '_')}.json"
    with open(file_path, "w") as f:
        json.dump(data, f, indent=4)
    print(f"[+] Specifiche salvate in {file_path}")
