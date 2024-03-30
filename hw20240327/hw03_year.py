def is_leap_year(y):
    if y % 4 == 0:
        if y % 100:
            return False
        else:
            return True
    else:
        return False

def main():
    y = int(input("윤년임을 확인할 년도를 입력하세요 : "))
    if is_leap_year(y):
        print(f"{y}년은 윤년입니다.")
    else:
        print(f"{y}년은 평년입니다.")

if __name__ == "__main__":
    main()