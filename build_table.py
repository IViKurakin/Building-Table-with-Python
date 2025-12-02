from prettytable import PrettyTable
import matplotlib.pyplot as diagram

receipt = PrettyTable()
receipt.field_names = ['№','Продукт','Цена','Количество','Стоимость']

products = []
pay = []

for i in range(3):
    product = input('Укажите название продукта: ')
    price = int(input('Введите цену продукта: '))
    quantity = int(input('Укажите количество продукта: '))
    receipt.add_row([i+1, product, f'{price} руб.', f'{quantity} шт.', f'{price*quantity} руб.'])
    products.append(product)
    pay.append(price*quantity)

print(receipt)
diagram.bar(products, pay)
diagram.show()