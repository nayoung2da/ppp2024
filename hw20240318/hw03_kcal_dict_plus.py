calories = {"한라봉":0.5, "딸기":0.34, "바나나":0.77, "감":0.51, "망고":0.61, "리치":0.61, "복숭아":0.49, "블루베리":0.48, "사과":0.58}

fruits = input("먹은 과일의 이름을 입력하세요. : ")
g = int(input("{} 섭취량(g기준)을 입력하세요. : ".format(fruits)))

if fruits in calories:
    total_calories = calories[fruits] * g
    print("=" * 12, "결과", "=" * 12)
    print("{} {}g의 칼로리는 {}kcal입니다.".format(fruits, g, total_calories))
else:
    print("과일 {}에 대한 칼로리 정보가 없습니다. 죄송합니다.".format(fruits))