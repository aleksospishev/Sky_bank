import logging
from typing import Any, Dict, List

import pandas as pd

read_file_logger = logging.getLogger(__name__)
file_handler = logging.FileHandler("./logs/read_file.log", mode="w")
file_formatter = logging.Formatter("%(asctime)s %(filename)s %(levelname)s: %(message)s")
file_handler.setFormatter(file_formatter)
read_file_logger.addHandler(file_handler)
read_file_logger.setLevel(logging.DEBUG)


def csv_or_xls_read_file(file_name: str) -> List[Dict[str, Any]]:
    """Функция принимает путь до файла .csv или .xlsx(xls) возвращает содержимое списоком словарей."""

    try:
        read_file_logger.info(f"Считываем данные из файла {file_name} ")
        if ".csv" in file_name:
            df = pd.read_csv(file_name, delimiter=";")
            df = df.fillna("")
            data = df.to_dict(
                orient="records",
            )
        elif ".xls" in file_name:
            df = pd.read_excel(file_name)
            df = df.fillna("")
            data = df.to_dict(orient="records")
        else:
            read_file_logger.warning("Файл имеет разрешение отличное от xls или csv")
            data = []
        return data
    except FileNotFoundError as e:
        read_file_logger.warning(e)
        return "файл не найден введите корректный путь"
