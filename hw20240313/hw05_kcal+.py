hallabing = 0.5
strawberry = 0.34
banana = 0.77
gam = 0.51
mango = 0.61
rich = 0.61
peach = 0.49
blueberry = 0.48
apple = 0.58

fruits = input("먹은 과일의 이름을 영어로 입력하세요. : ")
g = int(input("{} 섭취량(g기준)을 입력하세요. : ".format(fruits)))

hallabing_kcal = 0.5 * g
strawberry_kcal = 0.34 * g
banana_kcal = 0.77 * g
gam_kcal = 0.51 * g
mango_kcal = 0.61 * g
rich_kcal = 0.61 * g
peach_kcal = 0.49 * g
blueberry_kcal = 0.48 * g
apple_kcal = 0.58 * g

if fruits == 'hallabing':
    print("한라봉 {}g의 칼로리는 {}kcal입니다.".format(g, hallabing_kcal))
elif fruits == 'strawberry':
    print("딸기 {}g의 칼로리는 {}kcal입니다.".format(g, strawberry_kcal))
elif fruits == 'banana':
    print("바나나 {}g의 칼로리는 {}kcal입니다.".format(g, banana_kcal))
elif fruits == 'gam':
    print("감 {}g의 칼로리는 {}kcal입니다.".format(g, gam_kcal))
elif fruits == 'mango':
    print("망고 {}g의 칼로리는 {}kcal입니다.".format(g, mango_kcal))
elif fruits == 'rich':
    print("리치 {}g의 칼로리는 {}kcal입니다.".format(g, rich_kcal))
elif fruits == 'peach':
    print("복숭아 {}g의 칼로리는 {}kcal입니다.".format(g, peach_kcal))
elif fruits == 'blueberry':
    print("블루베리 {}g의 칼로리는 {}kcal입니다.".format(g, blueberry_kcal))
elif fruits == 'apple':
    print("사과 {}g의 칼로리는 {}kcal입니다.".format(g, apple_kcal))
else:
    print("과일 {}에 대한 칼로리 정보가 없습니다. 죄송합니다.".format(fruits))