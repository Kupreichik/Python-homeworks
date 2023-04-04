# Винни-Пух попросил Вас посмотреть, есть ли в его стихах ритм. Поскольку разобраться в его кричалках не
# настолько просто, насколько легко он их придумывает, Вам стоит написать программу. Винни-Пух считает, что
# ритм есть, если число слогов (т.е. число гласных букв) в каждой фразе стихотворения одинаковое. Фраза может
# состоять из одного слова, если во фразе несколько слов, то они разделяются дефисами. Фразы отделяются друг 
# от друга пробелами. Стихотворение  Винни-Пух вбивает в программу с клавиатуры. В ответе напишите “Парам 
# пам-пам”, если с ритмом все в порядке и “Пам парам”, если с ритмом все не в порядке

# *Пример:*

# **Ввод:** пара-ра-рам рам-пам-папам па-ра-па-да
#     **Вывод:** Парам пам-пам

def look_for_rhythm(phrase):
  vowels = 'аеёиоуыэюя'
  count_vowels = lambda x: sum(1 for i in x if i in vowels)
  count_list = list(map(count_vowels, phrase.split()))
  print('Парам пам-пам') if all([i == count_list[0] for i in count_list]) else print('Пам парам')

look_for_rhythm('пара-ра-рам рам-пам-папам па-ра-па-да')