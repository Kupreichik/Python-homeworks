def create_list():
  num_list = []
  item = input('Введите число. Если числа закончились, введите "end" ')

  try:
    while item != 'end':
        num_list.append(float(item))
        item = input('Введите число. Если числа закончились, введите "end" ')
  except:
    print('Нужно вводить числа')
  
  return num_list