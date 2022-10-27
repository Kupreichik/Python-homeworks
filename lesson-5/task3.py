# задача 3. Напишите программу, удаляющую из текста все слова, содержащие "абв".
#  Функции FIND и COUNT юзать нельзя.

def delete_words(text, substring):
  try:
    text_ls = text.split()
    text_ls = list(filter(lambda word: not substring in word, text_ls))
    res = ' '.join(text_ls)
    print(res)
  except:
    print('Некорректные данные, не удалось обработать')

text = 'Ускоренная обработка дабвнных: lambdабв, filter, map, zip, enumerабвte, абвlist comprehensionабв'
substr = 'абв'

delete_words(text, substr)
