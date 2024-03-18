weight = float(input("몸무게를 입력해 주세요.(kg) : "))
height = float(input("키를 입력해 주세요.(cm) : "))
BMI = weight / (height/100)**2

print("*"*12, "결과", "*"*12)
print(f"BMI지수 : {weight / (height/100)**2}")
if BMI >= 35:
    print("당신은 3단계 비만입니다.")
elif BMI >= 30 and BMI < 35:
    print("당신은 2단계 비만입니다.")
elif BMI >= 25 and BMI < 30:
    print("당신은 1단계 비만입니다.")
elif BMI >= 23 and BMI < 25:
    print("당신은 비만 전단계입니다.")
elif BMI >= 18.5 and BMI < 23:
    print("당신은 정상체중입니다.")
else :
    print("저체중입니다.")