hallabing = int(input("한라봉 섭취량(g 기준)를 입력해주세요. : "))
strawberry = int(input("딸기 섭취량(g기준)을 입력해주세요. : "))
banana = int(input("바나나 섭취량(g기준)을 입력해주세요. :" ))

kcal = (hallabing * 0.5) + (strawberry * 0.34) + (banana * 0.77)
print("한라봉 {}g, 딸기 {}g, 바나나 {}g 섭취 시 칼로리는 {}kcal입니다.".format(hallabing, strawberry, banana, kcal))