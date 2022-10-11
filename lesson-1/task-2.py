# задача 2. Напишите программу для проверки истинности утверждения
#  ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат.

x = bool(input('Введите 1 или 0 для Х: '))
y = bool(input('Введите 1 или 0 для Y: '))
z = bool(input('Введите 1 или 0 для Z: '))

result = (not (x or y or z)) == (not x and not y and not z)
if result:
  print('Выражение истинно')
else:
  print('Выражение ложно')