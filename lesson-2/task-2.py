# Задача 2. Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.

# *Пример:*
# - пусть N = 4, тогда [ 1, 2, 6, 24 ] (1, 1*2, 1*2*3, 1*2*3*4)

def multipli_N_numbers():
  
  try:

    N = int(input('Ведите число: '))
    if N < 0:
      result = 'Нужно вводить целое неотрицательное число'
    elif N == 0:
      result = 0
    else:
      result = []
      for i in range(N):
        item = 1
        for j in range(N - i):
          item *= (j + 1)
        result.insert(0, item)
    print(result)

  except:
    print('Нужно вводить целое число')

multipli_N_numbers()