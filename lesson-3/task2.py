# Задача 2. Напишите программу, которая найдёт произведение пар чисел списка.
# Парой считаем первый и последний элемент, 
# второй и предпоследний и т.д.

#*Пример:*
#- [2, 3, 4, 5, 6] => [12, 15, 16];
#- [2, 3, 5, 6] => [12, 15]

import math
import create_list as fun

def multi_pairs(num_list = None):
  if not num_list:
    num_list = fun.create_list()

  result = []

  try:

    for i in range(math.ceil(len(num_list)/2)):
      result.append(num_list[i] * num_list[len(num_list) - (1 + i)])

  except:
    print('Переданы некорректные данные')

  print(result)

multi_pairs([2, 3, 4, 5, 6])
multi_pairs([2, 3, 5, 6])