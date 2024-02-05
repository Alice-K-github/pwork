import json
import datetime


"""загружаем данные с файла"""
def operations():
    with open("operations.json", 'r', encoding='utf-8-sig') as file:
        operations_json = json.load(file)
    return operations_json




""""Сортировка списка по статусу "выполнено" И дате (сначала новые)"""
def sort():
    operations_json = operations()
    operations_sorted1 = []
    for i in operations_json:
        if i.get("state") == "EXECUTED":
            operations_sorted1.append(i)
    operations_sorted2 = sorted(operations_sorted1, key=lambda x: x.get("date"), reverse=True)
    return operations_sorted2


"""Срез - последние 5 выполненных операций"""
def cuts():
    operations_sorted2 = sort()
    listo = operations_sorted2[0:5]
    return listo

"""Преобразование даты в привычный формат (из отсортированного, обрезанного списка) ПО ИНДЕКСУ"""
def data(i, listo):

    data = listo[i]["date"]
    dt = datetime.datetime.strptime(data, '%Y-%m-%dT%H:%M:%S.%f')
    return dt
    #print(f"{dt:%d.%m.%Y}")

"""def if_from(i, listo):
    if listo[i].get("from") in listo:
        return True
    else:
        return False"""


"""Получаем карту и счёт отправителя """
def count(i, listo):
    count_ = listo[i].get("from")
    return count_

def split_card(card):
    #смотри решение на сайте

