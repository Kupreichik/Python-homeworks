# задача 1. Создайте программу для игры с конфетами человек против человека.
# Условие задачи: На столе лежит 2021 конфета. Играют два игрока делая ход друг после друга. Первый ход определяется жеребьёвкой. За один ход можно забрать не более чем 28 конфет. Все конфеты оппонента достаются сделавшему последний ход. Сколько конфет нужно взять первому игроку, чтобы забрать все конфеты у своего конкурента?
# Делаем игру против бота.  Подумайте как наделить бота ""интеллектом""

import random

def start():
  answer = input('Привет! Сыграем в конфеты? Их у меня 2021 штука! Ответь да или нет: ')
  yes = ['yes', 'Yes', 'YES', 'ok', 'да', 'Да', 'ДА']
  no = ['no', 'No', 'NO', 'Нет', 'нет', 'не', 'НЕТ']
  if answer in yes:
    game()
  elif answer in no:
    print('Как хочешь...')
  else:
    print('Не понял...')

def game():
  candys = 2012
  if random.randint(0, 2):
    print('Жеребьёвка определила, что ты ходишь первым!')
    n = ask_count()
    candys = candys_count(candys, n)

  else:
    print('Жеребьёвка определила, что первым хожу я!')
    n = random.randint(1, 28)
    print('Я возьму ', n)
    candys = candys_count(candys, n)
    n = ask_count()
    candys = candys_count(candys, n)

  while candys > 57:
    n = random.randint(1, 28)
    print('А я возьму ', n)
    candys = candys_count(candys, n)
    n = ask_count()
    candys = candys_count(candys, n)

  if candys > 29:
    n = candys - 29
    print('А я возьму ', n)
    candys = candys_count(candys, n)
    n = ask_count()
    candys = candys_count(candys, n)
    print('А я заберу все оставшиеся и я победил!!!')
  
  elif candys == 29:
    print('Ну вот(( Я возьму одну, а ты забирай оставшиеся, ты победил!!!')

  else:
    print('Я заберу все оставшиеся и я победил!!!')


def candys_count(candys, n):
  count = candys - n
  print('Конфет осталось ', count)
  return count

def ask_count():
  try:
    n = int(input('Твой ход. Сколько берёшь конфет?: '))
    while 0 > n > 28:
      n = int(input('Играй по правилам! Бери не меньше 1 и не больше 28! Сколько берёшь?: '))
    return n
  except:
    print('Нужно вводить целые числа от 1 до 28')
    ask_count()

start()