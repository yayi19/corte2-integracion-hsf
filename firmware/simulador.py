import json
import random
import time
import os
from datetime import datetime

ruta_actual = os.path.dirname(os.path.abspath(__file__))
ruta_json = os.path.join(ruta_actual, "..", "data", "telemetria.json")

while True:

    datos = {
        "device_id": "ESP32_SIM_001",
        "temperature": random.randint(20, 45),
        "humidity": random.randint(30, 90),
        "cpu": random.randint(10, 100),
        "timestamp": str(datetime.now())
    }

    with open(ruta_json, "w") as archivo:
        json.dump(datos, archivo, indent=4)

    print("Datos enviados:", datos)

    time.sleep(5)