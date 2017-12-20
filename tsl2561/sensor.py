from tsl2561 import TSL2561


def read_data():
    tsl = TSL2561()
    return {"lux": float(tsl.lux())}
