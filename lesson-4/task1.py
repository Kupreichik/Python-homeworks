# задача 1. Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.

def get_prime_divisors(n):
  try:
    divisors = []
    div = 2

    while(div <= n):
      if n % div == 0:
        divisors.append(div)
        n = n / div
      else:
        div += 1
  except:
    print('Переданы некорректные данные')

  print(divisors)

try:
  n = int(input('Введите число: '))
  get_prime_divisors(n)
except:
  print('Нужно вводить целое число')