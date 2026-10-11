import platform
import psutil
import shutil

def obtener_sistema():

    memoria = psutil.virtual_memory()

    disco = shutil.disk_usage("/")

    info = {
        "sistema_operativo": platform.system(),
        "version": platform.release(),
        "memoria_disponible_gb": round(memoria.available / (1024**3), 2),
        "disco_libre_gb": round(disco.free / (1024**3), 2)
    }

    return info