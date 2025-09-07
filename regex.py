import re

# Сюда грузим адреса
sourceString = """
РФ, Смоленск, ул. Шевченко, д. 65, кв 34
РФ, Смоленск, ул. Шевченко, д. 65, кв 35
г. Москва, ул. Сущёвский вал, д. 25, пом. 14, комната №10-15
РФ, Республика Татарстан, Казань, ул. Островского, 31, Магазин "Пятерочка"
г. Владивосток, улица Ивановская, дом 5, 1-4 этажи
"""

# Создаем список, разделив на адреса по переносам строк
addresses = sourceString.strip().split('\n')

# Обрабатываем каждый адрес отдельно
processed_addresses = []
for address in addresses:
# re.sub(шаблон, на что заменяем, сами строки, flags) 
    match = re.sub(r',\s*(пом|кв\.|магазин).*', "", address, flags=re.IGNORECASE)
    processed_addresses.append(match)

# Объединяем с разделителем " ---> "
pre_result = [' -----> '.join(x) for x in zip(addresses, processed_addresses)]

# Выводим список без квадратных скобок
result = '\n'.join(str(i) for i in pre_result)

print(result)

