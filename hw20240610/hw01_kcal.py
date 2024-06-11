import os
import requests
import numpy as np

DB_FILE = "./cal_db.csv"

def total_calorie(food, eat_calorie_dic):
    total_calorie = 0
    for food, weight in food.items():
        if food in eat_calorie_dic:
            total_calorie += weight*eat_calorie_dic[food]/100
        else:
            print(f"{food}의 칼로리 정보가 없습니다.")
    return total_calorie

def read_cal_db(filename):
    database = {}
    with open(filename) as f:
        lines = f.readlines()
        
        for line in lines[1:]:
            tokens = line.split(",")
            food_name = tokens[0]
            food_cal = int(tokens[1])
            database[food_name] = food_cal
    return database

def read_db():
    kcal_db = []
    if not os.path.exists(DB_FILE):
        return kcal_db
    
    with open(DB_FILE) as f:
        kcal_db = [float(x) for x in f.readlines().split(",")]
    return kcal_db

def write_db(kcal_db):
    with open(DB_FILE, "w") as fout:
        for x in kcal_db:
            #fout.write(f"{x}\n")
            fout.write(",".join(map(str, kcal_db)))


def main():
    eat_calorie_dic = read_cal_db("hw20240610/calorie_db.csv")
    kcal_total = read_db()
    print(f"현재까지 먹은 오늘의 칼로리 : {kcal_total}")
        food = float(input("추가할 음식 이름을 입력하세요. : "))
        if food < 0:
            break
        kcal_total.append(food)
    print(f"현재까지 먹은 오늘의 칼로리 : {kcal_total}")
    print(f"권장칼로리 섭취량 {}kcal에서 더 섭취할 수 있는 칼로리는 {np.average(kcal_total):.2f}입니다.")

    write_db(kcal_total)


if __name__ == "__main__":
    main()