import csv
import os

def guardar_csv(datos, estado):

    archivo = "../data/reporte.csv"

    existe = os.path.isfile(archivo)

    with open(archivo, "a", newline="") as csvfile:

        writer = csv.writer(csvfile)

        if not existe:
            writer.writerow([
                "device_id",
                "temperature",
                "humidity",
                "cpu",
                "timestamp",
                "estado"
            ])

        writer.writerow([
            datos["device_id"],
            datos["temperature"],
            datos["humidity"],
            datos["cpu"],
            datos["timestamp"],
            estado
        ])