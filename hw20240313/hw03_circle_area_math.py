import math

r = int(input("원의 반지름을 입력하세요. : "))
area = math.pi * math.pow(r, 2)

print("반지름이 {}인 원의 넓이는 {}입니다.".format(r, area))