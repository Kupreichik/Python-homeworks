# Задача 3. Задайте список из вещественных чисел. Напишите программу, 
# которая найдёт разницу между максимальным и минимальным значением дробной части элементов.

# *Пример:*
# - [1.1, 1.2, 3.1, 5, 10.01] => 0.19

import create_list as fun

def diff_max_min(list = None):
  if not list:
    list = fun.create_list()

  list1 = []

  try:

    for i in range(len(list)):
      if list[i] % 1 == 0:
        continue
      n = len(str(list[i]).split('.')[-1])
      list1.append(round(list[i] % 1, n))

    r = max(list1) - min(list1)
    print(r)
  
  except:
    print('Переданы некорректные данные')

diff_max_min([1.1, 1.2, 3.1, 5, 10.01])