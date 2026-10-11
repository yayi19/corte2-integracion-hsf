import json
import logging

from procesador import validar
from procesador import analizar
from monitor_so import obtener_sistema
from exportador import guardar_csv

logging.basicConfig(
    filename="../logs/sistema.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

try:

    with open("../data/telemetria.json", "r") as archivo:
        datos = json.load(archivo)

    if validar(datos):

        estado = analizar(datos)

        guardar_csv(datos, estado)

        sistema = obtener_sistema()

        logging.info("Datos procesados correctamente")

        print("\n=== DATOS DE TELEMETRIA ===")
        print(datos)

        print("\n=== INFORMACION DEL SISTEMA ===")
        print(sistema)

        print("\n=== ESTADO ===")
        print(estado)

    else:

        logging.warning("Datos invalidos")
        print("Datos invalidos")

except Exception as e:

    logging.error(str(e))
    print("Error:", e)