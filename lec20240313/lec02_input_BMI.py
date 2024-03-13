height = int(input("키를 입력해주세요. : "))
weight = int(input("몸무게를 입력해주세요. : "))
BMI = weight / (height/100)**2

# 소수점 작성 원할 땐 int => float
# height = float(input("키를 입력해주세요. : "))
# weight = float(input("몸무게를 입력해주세요. : "))
# BMI = weight / (height/100)**2

print("*"*12, "결과", "*"*12)
print("BMI지수 : {}".format(BMI))