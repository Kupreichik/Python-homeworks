# Требуется найти в массиве A[1..N] самый близкий по величине элемент к заданному числу X.
# Пользователь в первой строке вводит натуральное число N – количество элементов в массиве.
# В последующих  строках записаны N целых чисел Ai. Последняя строка содержит число X

# *Пример:*

# 5
# 1 2 3 4 5
# 6
# -> 5

try:
  n = int(input('Введите количество элементов в массиве: '))
  num_list = [int(i) for i in input('Введите числа через пробел: ').split(' ')]
  x = int(input('Введите искомое число: '))

  res = num_list[0]

  for i in num_list:
    if abs(i - x) < abs(res - x):
      res = i

  print(f'Ближайшее число к искомому {res}')

except:
  print('Введены некорректные данные')