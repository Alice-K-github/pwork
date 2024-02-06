from utils.functions import cuts, data, format_card, is_none, description, to_count, sum_

listo = cuts()
for i in range(len(listo)):
    dt = data(i, listo)
    des = description(i, listo)
    print(f"{dt:%d.%m.%Y} {des}")
    name_to, to_ = to_count(i, listo)
    if is_none(i, listo):
        name_card, num_card = format_card(i, listo)
        print(f"{name_card} {num_card} -> {name_to} {to_}")
    else:
        print(f"{name_to} {to_}")
    amount, name = sum_(i, listo)
    print(f"{amount} {name}")
    print(" ")