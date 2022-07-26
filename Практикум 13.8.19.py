total_cost = 0
while True:
    try:
        ticket_amount = input('Сколько билетов вы хотите приобрести на мероприятие? ')
        ticket_amount = int(ticket_amount)
        if type(ticket_amount) == int:
            break
    except ValueError:
        print('Введите целое число')
for i in range(ticket_amount):
    i += 1
    while True:
        try:
            age = input(f'Для какого возраста билет №{i}? ')
            age = int(age)
            if age < 18:
                print('Билет бесплатный')
            elif 25 > age >= 18:
                total_cost += 990
                print('Стоимость билета: 990 руб.')
            else:
                total_cost += 1390
                print('Стоимость билета: 1390 руб.')
            if type(age) == int:
                break
        except ValueError:
            print('Введите целое число')
if ticket_amount > 3:
    total_cost = total_cost - ((total_cost / 100) * 10)
    print(f'Сумма к оплате {total_cost} руб. с учетом 10%-ой скидки на полную стоимость заказа за регистрацию больше 3х человек')
else:
    print(f'Сумма к оплате {total_cost} руб.')