# задача 4 HARD необязательная Напишите простой калькулятор, который считывает с пользовательского ввода три строки: первое число, второе число и операцию, после чего применяет операцию к введённым числам ("первое число" "операция" "второе число") и выводит результат на экран.

# Поддерживаемые операции: +, -, /, *, mod, pow, div, где
# mod — это взятие остатка от деления,
# pow — возведение в степень,
# div — целочисленное деление.

# Если выполняется деление и второе число равно 0, необходимо выводить строку "Деление на 0!".

# Обратите внимание, что на вход программе приходят вещественные числа.

try:
  int_1 = float (input('Введите первый операнд: '))
  int_2 = float (input('Введите второй операнд: '))
  operation = str (input('Введите операцию (+, -, /, *, mod, pow, div): '))

  if operation == '+':
    print(int_1 + int_2)
  elif operation == '-':
    print(int_1 - int_2)
  elif operation == '*':
    print(int_1 * int_2)
  elif operation == '/' and int_2 == 0:
    print("Деление на 0!")
  elif operation =='/' and int_2 != 0:
    print(int_1 / int_2)
  elif operation =='mod' and int_2 == 0:
    print('Деление на 0!')
  elif operation =='mod' and int_2 != 0:
    print(int_1 % int_2)
  elif operation =='pow':
    print(int_1 ** int_2)
  elif operation =='div' and int_2 == 0:
    print('Деление на 0!')
  elif operation =='div' and int_2 != 0:
    print(int_1 // int_2)
  else:
    print('Операция введена некорректно или не поддерживается')
except:
  print('Нужно вводить числа')