    
def cal_calories(type):
    calories = {"한라봉":0.5, "딸기":0.34, "바나나":0.77, "감":0.51, "망고":0.61, "리치":0.61, "복숭아":0.49, "블루베리":0.48, "사과":0.58}
    eat_fruits = []
    for i in range(type):
        fruit = input("먹은 과일의 이름을 입력하세요: ")
        amount = float(input(f"{fruit}의 먹은 양을 입력하세요(그램 단위): "))
        eat_fruits.append((fruit, amount))

    total_calories = 0
    for fruit, amount in eat_fruits:
        if fruit in calories:
            total_calories += calories[fruit] * amount

    return(f"총 칼로리는 {total_calories}kcal입니다.")

def main():
    type = int(input("몇 종류의 과일을 드셨나요?(숫자만 입력해주세요.) : "))
    result = cal_calories(type)
    print(result)

if __name__=="__main__":
    main()