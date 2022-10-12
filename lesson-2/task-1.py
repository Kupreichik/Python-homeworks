# Задача 1. Напишите программу, которая принимает на вход вещественное или целое число и показывает сумму его цифр. Через строку нельзя решать.

# *Пример:*
# - 6782 -> 23
# - 0,56 -> 11

def is_number(string):
  try:
    string = string.replace(',', '.')
    float(string)
    return True
  except:
    return False

def sum_digits():
  number = input('Введите число: ')

  if is_number(number):
    digits = list(number)
    sum = 0
    for item in digits:
      if item.isdigit():
        sum += int(item)
    print(sum)

  else:
    print('Нужно вводить число')

sum_digits()