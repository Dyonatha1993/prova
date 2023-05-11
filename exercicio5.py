import random

d1 =random.randint(1, 6)

d2 =random.randint(1, 6)

d3 =random.randint(1, 6)



print(f'd1: {d1}')

print(f'd2: {d2}')

print(f'd3: {d3}')

if d1 > d2 and d1 > d3:

  print ('dado 1 é maior')

elif d2 > d1 and d2 > d3:

  print('dado 2 é o maior')

elif d3 > d1 and d3 > d2:

  print('dado 3 é o maio')

elif d1==d2 and d1==d3 and d2==d3:

  print('igualdade')

elif d1==d2 or d2==d3 or d3==d1:

  print('dupla igualdade sem numero maior')

