# Задача 4 НЕОБЯЗАТЕЛЬНАЯ. Напишите программу, 
# которая принимает на вход N, и координаты двух точек и 
# находит расстояние между ними в N-мерном пространстве.

import math
try:
  N = int(input("Введите значение N для N-мерного пространства: "))
  coordA = []
  for i in range(N):
      coordA.append(int(input("введите координату точки А: ")))
  coordB = []
  for i in range(N):
      coordB.append(int(input('введите координату точки В: ')))
  sum = 0
  for i in range(N):
    sum += ((coordB[i]- coordA[i])**2)
  distan = math.sqrt(sum)
  print(round(distan, 2))
except:
  print('Введите числа')