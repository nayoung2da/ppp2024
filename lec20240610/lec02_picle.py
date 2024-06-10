import os
import numpy as np
import pickle

#DB_FILE = "./grade_db.txt"
#DB_FILE = "./grade_db.csv"
DB_FILE = "./grade_db.pk1"

def read_db():
    grade_db = []
    if not os.path.exists(DB_FILE):
        return grade_db
    
    with open(DB_FILE, "rb") as f:
        #grade_db = [float(x) for x in f.readlines()]
        #grade_db = [float(x) for x in f.readlines().split(",")]
        grade_db = pickle.load(f)
    return grade_db

def write_db(grade_db):
    with open(DB_FILE, "wb") as fout: 
        pickle.dump(grade_db, fout)

def main():
    #grade_total = [3.5, 4.5]

    grade_total = read_db()
    print(f"현재까지 학점 목록은 {grade_total}입니다.")
    while True:
        grade = float(input("추가할 학점을 입력하세요. : "))
        if grade < 0:
            break
        grade_total.append(grade)
    print(f"현재까지 학점 목록은 {grade_total}입니다")
    print(f"평균학점은 {np.average(grade_total):.2f}입니다.")

    write_db(grade_total)


if __name__ == "__main__":
    main()