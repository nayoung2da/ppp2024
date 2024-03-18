calories = {"한라봉":0.5, "딸기":0.34, "바나나":0.77, "감":0.51, "망고":0.61, "리치":0.61, "복숭아":0.49, "블루베리":0.48, "사과":0.58}

eat_hallabong = int(input("한라봉 섭취량(g기준)을 입력해주세요. : "))
eat_strawberry = int(input("딸기 섭취량(g기준)을 입력해주세요. : "))
eat_banana = int(input("바나나 섭취량(g기준)을 입력해주세요. : "))
eat_gam = int(input("감 섭취량(g기준)을 입력해주세요. : "))
eat_mango = int(input("망고 섭취량(g기준)을 입력해주세요. : "))
eat_rich = int(input("리치 섭취량(g기준)을 입력해주세요. : "))
eat_peach = int(input("복숭아 섭취량(g기준)을 입력해주세요. : "))
eat_blueberry = int(input("블루베리 섭취량(g기준)을 입력해주세요. : "))
eat_apple = int(input("사과 섭취량(g기준)을 입력해주세요. : "))

total_calories = calories["한라봉"] * eat_hallabong + calories["딸기"] * eat_strawberry + calories["바나나"] * eat_banana + calories["감"] * eat_gam + calories["망고"] * eat_mango + calories["리치"] * eat_rich + calories["복숭아"] * eat_peach + calories["블루베리"] * eat_blueberry + calories["사과"] * eat_apple

print("=" * 12, "결과", "=" * 12)
print("총칼로리는 {}입니다.".format(total_calories))