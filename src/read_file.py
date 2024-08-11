import csv

import pandas as pd


def csv_or_xls_read_file(file_name):
    """Функция принимает путь до файла если файл разрешения .csv или .xlsx(xls) возвращает содержимое
    списоком словарей"""
    try:
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
            data = []
        return data
    except FileNotFoundError:
        return "файл не найден введите корректный путь"
