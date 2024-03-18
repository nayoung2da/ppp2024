import math

r = int(input("원의 반지름을 입력하세요. : "))
round = 2 * math.pi * r
area = math.pi * math.pow(r, 2)

print("=" * 12, "결과", "=" * 12)
print("반지름이 {}인 원의 둘레는 {:.1f}입니다.".format(r, round))
print("반지름이 {}인 원의 넓이는 {:.2f}입니다.".format(r, area))