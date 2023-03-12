# Требуется определить, можно ли от шоколадки размером n × m долек отломить k долек, если разрешается сделать один разлом по прямой между дольками (то есть разломить шоколадку на два прямоугольника).

# *Пример:*

# 3 2 4 -> yes
# 3 2 1 -> no

try:
  n, m, k = [int(item) for item in (input('Введите через пробел n, m, k: ').split(' '))]
  if k <= n * m and ((k % n == 0) or (k % m == 0)):
    print('yes')
  else:
    print('no')
except:
  print('Введены некорректные данные')
