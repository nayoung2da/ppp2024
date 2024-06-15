import os
import csv
import numpy as np

DB_FILE = "./eat_calorie_db.csv"

def read_db():
    if not os.path.exists(DB_FILE):
        return {}
    
    calorie_db = {}
    with open(DB_FILE, "r", encoding="utf-8") as f:
        reader = csv.reader(f)
        for row in reader:
            fruit = row[0]
            grams_list = list(map(int, row[1:]))
            calorie_db[fruit] = grams_list
    return calorie_db

def write_db(calorie_db):
    with open(DB_FILE, "w", encoding="utf-8") as fout:
        writer = csv.writer(fout)
        for fruit, grams_list in calorie_db.items():
            writer.writerow([fruit] + grams_list)

def total_calorie(fruits_eat, fruits_cal_dic):
    total = 0
    for fruit_name, grams in fruits_eat.items():
        if fruit_name in fruits_cal_dic:
            total += fruits_cal_dic[fruit_name] * grams / 100
        else:
            print(f"{fruit_name}의 정보를 찾을 수 없습니다.")
    return total

def read_cal_db(filename):
    database = {}
    with open(filename, encoding="utf-8-sig") as f:
        reader = csv.reader(f)
        next(reader)
        for row in reader:
            fruit_name = row[0]
            fruit_cal = float(row[1])
            database[fruit_name] = fruit_cal
    return database

def main():
    fruits_calorie_dic = read_cal_db("hw20240610/calorie_db.csv")
    
    fruits_eat = input("먹은 과일을 ,로 구분하여 모두 입력하세요: ").split(",")
    fruits_eat = {fruit.strip(): int(input(f"{fruit.strip()}의 먹은 양을 입력하세요(단위: g): ")) for fruit in fruits_eat}
    total = total_calorie(fruits_eat, fruits_calorie_dic)
    print(f"이번에 섭취 칼로리 총량은 {total:.2f} kcal입니다.")
    
    calorie_total = read_db()
    
    for fruit, grams in fruits_eat.items():
        if fruit in calorie_total:
            calorie_total[fruit].append(grams)
        else:
            calorie_total[fruit] = [grams]
    
    print(f"현재까지 섭취한 과일 목록과 섭취량: {calorie_total}")
    fruit_totals = {fruit: np.sum(grams_list) for fruit, grams_list in calorie_total.items()}
    
    print(f"현재까지 섭취한 과일의 총 섭취량: {fruit_totals}")
    write_db(calorie_total)

    total_calories = sum(total_calorie({fruit: total_grams}, fruits_calorie_dic) for fruit, total_grams in fruit_totals.items())
    print(f"현재까지의 총 섭취 칼로리: {total_calories:.2f} kcal")

if __name__ == "__main__":
    main()