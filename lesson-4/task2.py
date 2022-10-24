# задача 2 . Задайте последовательность чисел. Напишите программу, 
# которая выведет список неповторяющихся элементов исходной последовательности.

import create_list as fun

def get_unique_items(start_list = None):
  if not start_list:
    start_list = fun.create_list()

  try:
    uniques_list = list(set(start_list))
    print(uniques_list)
  except:
    print('Переданы некорректные данные')

get_unique_items([0, 3, 5, 0, 7, 7, 5, 4, 5, 5])
get_unique_items([0, 0.5, 0.5, 1, 1, 1, 0])