import math

height = int(input("키를 입력해주세요. : "))
weight = int(input("몸무게를 입력해주세요. : "))
BMI = weight / math.pow((height/100), 2)

print("*"*12, "결과", "*"*12)
print("BMI지수 : {}".format(BMI))
if BMI >= 25:
    print("당신은 비만입니다.")
elif BMI >= 23 and BMI < 25:
    print("당신은 과체중입니다.")
elif BMI >= 18.5 and BMI < 23:
    print("당신은 정상체중입니다.")
else :
    print("저체중입니다.")