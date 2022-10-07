tickets = int(input("При покупке 4-х билетов и более действует скидка 10% от стоимости заказа!\n"
                   "Укажите количество приобретаемых билетов:"))
age = list(map(int, input("Укажите через пробел возраст посетителей: ").split()))
while tickets != len(age):
    age = list(map(int, input("Неверно указано количество поситителей.\n"
                              "Укажите через пробел возраст посетителей: ").split()))
price = []
for i in age:
    if i in range(0,18):
        price.append(0)
    elif i in range(18,25):
        price.append(990)
    else:
        price.append(1390)

if tickets>3:
    print("Сумма к оплате с учетом скидки: ", sum(price) - ((sum(price)/100)*10), "рублей")
else:
    print("Сумма к оплате: ", sum(price), "рублей")