# Найдите сумму цифр трехзначного числа.

# *Пример:*

# 123 -> 6 (1 + 2 + 3)
# 100 -> 1 (1 + 0 + 0)

try:
  num = input('Введите трёхзначное число: ')
  a = int(num[0])
  b = int(num[1])
  c = int(num[2])
  print(f'Сумма цифр числа: {a + b + c}')
except:
  print('Введены некорректные данные')
