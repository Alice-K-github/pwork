import json
import datetime


"""загружаем данные с файла"""
def operations():
    with open("../src/operations.json", 'r', encoding='utf-8-sig') as file:
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


"""Получаем карту и счёт отправителя """
def count(i, listo):
    count_ = listo[i].get("from")
    return count_

"""Достаём, форматируем и шифруем номер карты"""
def number_card(card):
    card_number = card.split()[-1]
    private_number = card_number[:6] + (len(card_number[6:-4]) * '*') + card_number[-4:]
    chunks, chunk_size = len(private_number), len(private_number) // 4
    number = " ".join([private_number[i:i + chunk_size] for i in range(0, chunks, chunk_size)])
    return number

"""Наименование карты (виза, мастеркард и тп)"""
def name_card(card):
    name = " ".join(card.split(' ')[:-1])
    return name

"""Проверка на наличие from"""
def is_none(i, listo):
    if count(i, listo) is not None:
        return True
    else:
        return False

"""При наличии from записывает и возвращает наименование и зашифрованный счёт карты"""
def format_card(i, listo):
    if is_none(i, listo):
        card = count(i, listo)
        number_card_ = number_card(card)
        name_card_ = name_card(card)
        return name_card_, number_card_
    else:
        return False

"""Возвращает тип операции"""
def description(i, listo):
    des = listo[i]["description"]
    return des

"""Счёт отправителя\вклада, форматирование, вывод = наименование, номер в шифре"""
def to_count(i, listo):
    to = listo[i]["to"]
    to_cut = to.split()[-1]
    to_ = ''.join("**" + to_cut[:4])
    name_to = ''.join(to.split(' ')[:-1])
    return name_to, to_

"""Достаём из списка сумму и валюту"""
def sum_(i, listo):
    amount = listo[i]["operationAmount"]["amount"]
    name = listo[i]["operationAmount"]["currency"]["name"]
    return amount, name
