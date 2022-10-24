# задача 3. Задана натуральная степень k. 
# Сформировать случайным образом список коэффициентов (значения от 0 до 100) многочлена и записать в файл многочлен степени k.
# *Пример:* 
# - k=2 => 2*x² + 4*x + 5 = 0 или x² + 5 = 0 или 10*x² = 0

from ast import Str
import random

def write_file(data):
  with open('polynomial_degree_k.txt', 'w') as file:
    file.write(data)

def create_coefficient_ls(k):
  coefficients = [random.randint(0,101) for i in range(k + 1)]
  return coefficients


def create_str(k):
  cfcts = create_coefficient_ls(k)
  str_plm = ''
  if len(cfcts) < 1:
    str_plm = 'x = 0'
  else:
    for i in range(len(cfcts)):

      if i != len(cfcts) - 1 and cfcts[i] != 0 and i != len(cfcts) - 2:
        str_plm += (str(cfcts[i]) + '*x^' + str(k - i))
        if cfcts[i + 1] != 0:
          str_plm += ' + '

      elif i == len(cfcts) - 2 and cfcts[i] != 0:
        str_plm += str(cfcts[i]) + '*x'
        if cfcts[i + 1] != 0:
          str_plm += ' + '

      elif i == len(cfcts) - 1 and cfcts[i] != 0:
        str_plm += str(cfcts[i]) + ' = 0'

      else:
        str_plm += ' = 0'

  return str_plm

try:
  k = int(input("Введите натуральную степень k = "))
  write_file(create_str(k))
except:
  print('Переданы некорректные данные')