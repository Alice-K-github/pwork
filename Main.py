from functions import cuts, data, count

listo = cuts()
for i in range(len(listo)):
    dt = data(i, listo)
    print(f"{dt:%d.%m.%Y}")
    print(count(i, listo))
    if count(i, listo) is not None:
        card = count(i, listo)
