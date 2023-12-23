from datetime import datetime
from PySide6.QtWidgets import QLabel, QListWidget
from src.client.api.resolver import getAll

def update_statistics(complete: QLabel, avg: QLabel, types: QListWidget):
    data = getAll("Requests")
    complete.setText(f"Количество выполненных заявок: {complete_sum(data)}")
    avg.setText(f"Среднее время выполнения заявки: {avg_completion_time(data)} дней")
    types.clear()
    disease_types(types, data)

def complete_sum(data: list):
    complete: int = 0
    for item in data:
        if not item["end_date"]: continue
        complete += 1
    return complete

def avg_completion_time(data: list):
    days: list = []
    date_format = "%d.%m.%Y"
    for item in data:
        if not item["end_date"]: continue
        add = datetime.strptime(item["add_date"], date_format).date()
        end = datetime.strptime(item["end_date"], date_format).date()
        delta = end - add
        days.append(delta.days)
    return sum(days) / len(days)

def disease_types(qlist: QListWidget, data: list):
    types: dict = {}
    for item in data:
        disease = item['disease_id']
        if types.__contains__(disease):
            types[disease] += 1
        else:
            types[disease] = 1
    for key, value in types.items():
        qlist.addItem(f"{key}: {value}")
