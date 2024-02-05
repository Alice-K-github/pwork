import json
import datetime

with open("operations.json", 'r', encoding='utf-8-sig') as file:
    operations_json = json.load(file)
data = operations_json[0]["date"]
dt = datetime.datetime.strptime(data, '%Y-%m-%dT%H:%M:%S.%f')
#print(f"{dt:%d.%m.%Y}")
operations_sorted1 = []

for i in operations_json:
    if i.get("state") == "EXECUTED":
        operations_sorted1.append(i)
operations_sorted2 = sorted(operations_sorted1, key=lambda x: x.get("date"), reverse=True)


listo = operations_sorted2[0:5]

data = listo[0]["date"]
dt = datetime.datetime.strptime(data, '%Y-%m-%dT%H:%M:%S.%f')
print(f"{dt:%d.%m.%Y}")


