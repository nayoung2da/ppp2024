#hw01-1
temp_c = 30.0
temp_f = temp_c * 9/5 +32
print("{}C ==> {}F".format(temp_c, temp_f))

#hw01-2
temp_c = 0.0
temp_f = temp_c * 9/5 +32
print("{}C ==> {}F".format(temp_c, temp_f))

#hw01+
temp_c = float(input("섭씨온도를 입력해주세요.:"))
temp_k = temp_c + 273.15
print(temp_c)
print("*"*12, "결과", "*"*12)
print(f"화씨온도 : {temp_c * 9/5 + 32}")
print(f"절대온도 : {temp_c + 273.15 }")
print(f"랭킨온도 : {temp_k * 9/5}")

#hw02
weight = 60
height = 170
BMI = weight / (height/100)**2
print(BMI)

#hw02+
weight = float(input("몸무게를 입력해 주세요.(kg) : "))
height = float(input("키를 입력해 주세요.(cm) : "))
BMI = weight / (height/100)**2

print("*"*12, "결과", "*"*12)
print(f"BMI지수 : {weight / (height/100)**2}")
if BMI >= 25:
    print("당신은 비만입니다.")
elif BMI >= 23 and BMI < 25:
    print("당신은 과체중입니다.")
elif BMI >= 18.5 and BMI < 23:
    print("당신은 정상체중입니다.")
else :
    print("저체중입니다.")

#hw03
pi = 3.141592
r = 4
원의넓이 = r * r * pi
print("반지름이 {}인 원의 넓이는 {}이다.".format(r, 원의넓이))

#hw04
base = 5
upper_side = 3
height = 4
trapezoid = base + upper_side * height / 2
print("사다리꼴의 넓이 : {}".format(trapezoid))
