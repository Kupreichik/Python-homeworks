# задача 2. Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.
# Входные и выходные данные хранятся в отдельных текстовых файлах.

def write_file(data, name):
  path = './lesson-5/' + name + '.txt'
  with open(path, 'w', encoding='utf-8') as file:
    file.write(data)

def rle_encode(path):
  try:
    with open(path, 'r', encoding='utf8') as file:
      data = file.read()
  except:
    print('Файл не найден')

  try:
    encoding_str = ''
    prev_char = ''
    count = 1

    if not data:
      encoding_str = 'False'

    for char in data:
      if char != prev_char:

        if prev_char:
          encoding_str += (str(count) + prev_char)

        count = 1
        prev_char = char

      else:
        count += 1 

    encoding_str += str(count) + prev_char
  except:
    print('Некорректные данные, не удалось обработать')

  write_file(encoding_str, 'task2_encoding')

def rle_decode(path):
  try:
    with open(path, 'r', encoding='utf8') as file:
      data = file.read()
  except:
    print('Файл не найден')

  try:
    decoding_str = ''
    count = ''

    for char in data:

      if char.isdigit():
        count += char
      else:
        decoding_str += char * int(count)
        count = ''
  except:
    print('Некорректные данные, не удалось обработать')
    write_file(decoding_str, 'task2_decoding')

rle_encode('./lesson-5/task2_str.txt')

rle_decode('./lesson-5/task2_encoding.txt')
