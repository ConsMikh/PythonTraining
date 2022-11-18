name = "Ada lovelace"

print(name.title())
print(name.upper())
print(name.lower())

# f-string
first_name = 'ada'
last_name = 'lovelace'
full_name_1 = f'{first_name} {last_name}'
print(full_name_1)
print(f'Hello, {full_name_1.title()}!')
full_name_2 = '{} {}'.format(first_name, last_name)
print(full_name_2)

# Убрать лишние пробелы по краям строки
extra_whitespaces = '   Extra     Whitespaces     string     '
print(extra_whitespaces.rstrip()) # Убрать пробелы справа от строки
print(extra_whitespaces.lstrip()) # Убрать пробелы слева от строки
print(extra_whitespaces.strip()) # Убрать пробелы слева и справа от строки

