def validar(datos):

    if datos["temperature"] < 0 or datos["temperature"] > 50:
        return False

    if datos["humidity"] < 0 or datos["humidity"] > 100:
        return False

    if datos["cpu"] < 0 or datos["cpu"] > 100:
        return False

    return True


def analizar(datos):

    if datos["temperature"] > 35:
        return "ANOMALIA TEMPERATURA"

    if datos["cpu"] > 90:
        return "ANOMALIA CPU"

    if datos["humidity"] > 85:
        return "ANOMALIA HUMEDAD"

    return "NORMAL"