def gugudan(dan):
    for i in range(2, 9+1):
        print(f"{dan} x {i} = {dan*i}")


if __name__=="__main__":
    dan = int(input("구구단 몇 단을 외울까요?(숫자만 입력해주세요.) : "))
    gugudan(dan)