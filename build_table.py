from prettytable import PrettyTable

receipt = PrettyTable()
receipt.field_names = ['№','Продукт','Цена','Количество','Стоимость']

print(receipt)
