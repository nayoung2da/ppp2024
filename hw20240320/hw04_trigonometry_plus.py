import math

trigon = input("sin, cos, tan 중 함수를 선택해주세요. : ")
degree = int(input(f"{trigon}함수의 값이 궁금한 각도를 입력해주세요 : "))

if trigon == "sin":
    a = math.sin(math.pi * degree/180)
    print(f"{trigon}함수 {degree}도 값은 {a:.3f}입니다.")
elif trigon == "cos":
    b = math.cos(math.pi * degree/180)
    print(f"{trigon}함수 {degree}도 값은 {b:.3f}입니다.")
else:
    c = math.tan(math.pi * degree/180)
    print(f"{trigon}함수 {degree}도 값은 {c:.3f}입니다.")