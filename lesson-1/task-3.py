# задача 3. Напишите программу, которая принимает на вход координаты точки (X и Y), и выдаёт номер четверти плоскости, в которой находится эта точка (или на какой оси она находится).

# *Пример:*
# - x=34; y=-30 -> 4
# - x=2; y=4-> 1
# - x=-34; y=-30 -> 3

try:
  x = int(input('Введите значение координат по оси x: '))
  y = int(input('Введите значение координат по оси y: '))

  if x > 0 and y > 0 :
    position = 'в 1 четверти'
  elif x < 0 and y > 0 :
    position = 'во 2 четверти'
  elif x < 0 and y < 0 :
    position = 'в 3 четверти'
  elif x > 0 and y < 0 :
    position = 'в 4 четверти'
  elif x == 0:
    position = 'на оси Х'
  else:
    position = 'на оси Y'
  
  print('Точка находится', position)
except:
  print('Нужно вводить целые числа')