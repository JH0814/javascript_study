import math
h, r = input('원기둥의 높이 h와 밑면의 반지름 r을 입력 : ').split()
h = float(h)
r = float(r)
a = 2 * h * r * math.pi + 2 * math.pi * r ** 2
print('높이가 %.2f이고 반지름이 %.2f인 원기둥의 겉넓이는 %.4e입니다' %(h, r, a))
p = a >= 10
print('원기둥의 겉넓이가 10 이상입니까?', p)