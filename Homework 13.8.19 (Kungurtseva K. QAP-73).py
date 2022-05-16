tickets = int(input("Введите количество билетов: "))
print("Укажите возраст каждого посетителя: ")
p = 0
for i in range(tickets):
    age = int(input("Возраст: "))
    if age < 18:
        p += 0
    elif 18 <= age < 25:
        p += 990
    else:
        p += 1390
if tickets > 3:
    f = 0.9
else:
    f = 1
print("Итоговая стоимость =", p*f)
