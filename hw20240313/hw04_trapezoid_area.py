print("사다리꼴의 넓이를 구하겠습니다.")
base = int(input("밑변의 길이를 입력하세요. : "))
upper_side = int(input("윗변의 길이를 입력하세요. : "))
height = int(input("높이를 입력하세요. : "))
trapezoid = (base + upper_side) * height / 2
print("밑변이 {}, 윗변이 {}, 높이가 {}인 사다리꼴의 넓이는 {}입니다.".format(base, upper_side, height, trapezoid))