# Задача 1 Задайте список из нескольких чисел.
#Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётной позиции.

# *Пример:*
# - [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12

import create_list as fun

def sum_even_items():
  num_list = fun.create_list()
  print(num_list)
  if len(num_list) < 2:
    return 0

  sum = 0

  for i in range(0, (len(num_list) - 1), 2):
    sum += num_list[i + 1]

  print(sum)

sum_even_items()