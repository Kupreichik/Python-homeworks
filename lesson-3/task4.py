# Задача 4. Напишите программу, которая будет преобразовывать 
# десятичное число в двоичное. Нельзя использовать готовые функции.

# *Пример:*
# - 45 -> 101101
# - 3 -> 11
# - 2 -> 10

def convert_decimal_to_binary(decimal):
  try:
    binary = ''

    while decimal != 0:
      binary = str(decimal % 2) + binary
      decimal = decimal // 2

    print(binary)
  except:
    print('Переданы некорректные данные')

dec = int(input('Введите число для перевода в двоичную систему счисления: '))
convert_decimal_to_binary(dec)