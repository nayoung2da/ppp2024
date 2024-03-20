#나영아 다 안 끝났다 다시 보렴..

calories = {"한라봉":0.5, "딸기":0.34, "바나나":0.77, "감":0.51, "망고":0.61, "리치":0.61, "복숭아":0.49, "블루베리":0.48, "사과":0.58}

eat_fruits = []
eat_fruits.append("한라봉")
eat_fruits.append("망고")

total_calories = 0
for item in eat_fruits:
    total_calories += eat_fruits[item]

fruits = input("먹은 과일의 이름을 입력하세요. : ")
g = int(input("{} 섭취량(g기준)을 입력하세요. : ".format(fruits)))

if fruits in calories:
    total_calories = calories[fruits] * g
    print("=" * 12, "결과", "=" * 12)
    print("{} {}g의 칼로리는 {}kcal입니다.".format(fruits, g, total_calories))
else:
    print("과일 {}에 대한 칼로리 정보가 없습니다. 죄송합니다.".format(fruits))

total_cost = 0
for item in cart:
    total_cost += mart[item]

print(f"담은 상품은 {cart}입니다.")
print(f"총 구매금액은 {total_cost:,}원입니다.")