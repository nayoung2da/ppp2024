def total_calorie(fruits, fruits_calorie_dic):
    total_calorie = 0
    for fruit, weight in fruits.items():
        if fruit in fruits_calorie_dic:
            total_calorie += weight*fruits_calorie_dic[fruit]/100
        else:
            print(f"{fruit}의 칼로리 정보가 없습니다.")
    return total_calorie


def read_cal_db(filename):
    database = {}
    with open(filename) as f:
        lines = f.readlines()
        
        for line in lines[1:]:
            tokens = line.split(",")
            fruit_name = tokens[0]
            fruit_cal = int(tokens[1])
            database[fruit_name] = fruit_cal
    return database

def main():
    fruits_calorie_dic = read_cal_db("hw20240408/calorie_db.csv")
    fruits_eat = input("먹은 과일을 ,로 구분하여 모두 입력하세요 : ").split(",")
    fruits_eat = {fruit: int(input(f"{fruit}의 먹은 양을 입력하세요(g 단위) : "))for fruit in fruits_eat}
    total = total_calorie(fruits_eat, fruits_calorie_dic)
    print(f"총칼로리는 {total}kcal입니다.")

if __name__ == "__main__":
    main()