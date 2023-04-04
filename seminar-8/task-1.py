# Дополнить телефонный справочник возможностью изменения и удаления данных. 
# Пользователь также может ввести имя или фамилию, и Вы должны реализовать 
# функционал для изменения и удаления данных

except_message = 'Ой! Что-то пошло не так... Попробуйте снова'

def manage_phonebook():
  try:
    operation = input('\nДобро пожаловать в телефонный справочник! \nМеню операций: \n1 - посмотреть весь справочник \n2 - найти запись \n3 - добавить запись \n4 - изменить запись \n5 - удалить запись \n# - выход\nВведите код операции: ')
    match operation:
      case '1': read_file()
      case '2': find_line()
      case '3': add_to_file()
      case '4': change_file()
      case '5': delete_line()
      case '#': return
    manage_phonebook()
  except:
    print(except_message)

def read_file():
  print()
  try:
    with open(path_file,'r',encoding='UTF-8') as f:
      for line in f:
        print(line.strip())
  except:
    print(except_message)

def add_to_file():
  print()
  try:
    new_info = []
    directives = ['Введите фамилию: ', 'Введите имя: ', 'Введите отчество: ', 'Введите номер телефона: ']

    for i in directives:
      data = input(i)
      if data == '#': return
      new_info.append(data)

    new_info = (' ').join(new_info).strip()

    with open(path_file,'a',encoding='UTF-8') as f:
      f.writelines('\n' + new_info)

    print(f'Данные "{new_info}" сохранены успешно')
  except:
    print(except_message)

def find_line():
  print()
  try:
    find_info = input('Введите данные для поиска: ')
    with open(path_file,'r',encoding='UTF-8') as f:
      for line in f:
        if find_info.casefold() in line.casefold():
          print(line)
  except:
    print(except_message)

def find_line_for_modify():
  print()
  try:
    res = []
    find_info = input('Введите данные для поиска: ')

    if find_info == '#': return '#'

    with open(path_file,'r',encoding='UTF-8') as f:
      for line in f:
        if find_info.casefold() in line.casefold():
          res.append(line)

    if len(res) == 1:
      print(res[0])
      return res[0]
    elif len(res) > 1:
      for i in range(len(res)):
          print(f'{i + 1} - {res[i]}')
      num_count = int(input('Выберите номер контакта, который нужно изменить/удалить: '))
      print(res[num_count - 1])
      return res[num_count - 1]
    else:
      print('По введённым данным ничего не найдено')
      return '#'

  except:
    print(except_message)

def change_file():
  try:
    phonebook = ''
    changing_line = find_line_for_modify()
    if changing_line == '#': return

    changing_line_list = changing_line.split()
    print('Какое поле вы хотите изменить?')
    field = input('1 - Фамилия\n2 - Имя\n3 - Отчество\n4 - Номер телефона\n')
    if field == '#': return
    text = ''
    match field:
      case '1': text = 'Фамилию'
      case '2': text = 'Имя'
      case '3': text = 'Отчество'
      case '4': text = 'номер телефона'
      case _: return

    new_field = input(f'Введите {text}: ')
    if new_field == '#': return
    changing_line_list[int(field) - 1] = new_field

    with open(path_file,'r',encoding='UTF-8') as f:
      phonebook = f.read()

    phonebook = phonebook.replace(changing_line, ' '.join(changing_line_list) + '\n')

    with open(path_file,'w',encoding='UTF-8') as f:
      f.write(phonebook)

    print('Данные успешно изменены')

  except:
    print(except_message)

def delete_line():
  try:
    phonebook = ''
    changing_line = find_line_for_modify()
    if changing_line == '#': return

    confirm = input(f'Для подтверждения удаления данных нажмите 1, для отмены #: ')

    if confirm != '1': return

    with open(path_file,'r',encoding='UTF-8') as f:
      phonebook = f.read()
    phonebook = phonebook.replace(changing_line, '')
    with open(path_file,'w',encoding='UTF-8') as f:
      f.write(phonebook)

    print('Данные успешно удалены')

  except:
    print(except_message)

def main():
  manage_phonebook()

path_file = r'phonebook.txt'
if __name__ == '__main__':
  main()