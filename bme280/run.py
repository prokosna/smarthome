import json
import logging
import logging.handlers
import os
from datetime import datetime, timezone

import sensor


def main():
    logger = logging.getLogger()
    logger.setLevel(logging.INFO)

    formatter = logging.Formatter("%(message)s")

    file_path = "{}/records/bme280.json.log".format(os.path.dirname(os.path.realpath(__file__)))

    trh = logging.handlers.TimedRotatingFileHandler(
        filename=file_path,
        when="D",
        backupCount=30,
        delay=True,
    )
    trh.setLevel(logging.INFO)
    trh.setFormatter(formatter)

    logger.addHandler(trh)

    data = sensor.read_data()
    data["@timestamp"] = datetime.now(timezone.utc).astimezone().isoformat()
    logger.info(json.dumps(data))


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        pass
