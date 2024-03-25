dan = int(input("구구단 몇 단을 출력할까요?(숫자만 입력해주세요.) : "))

print(f"구구단 {dan}단을 외워봅시다 ~")
for i in range(9):
    i = i + 1
    gugudan = dan * i
    print(f"{dan} x {i} = {gugudan}")

#for i in range(1, 9 + 1):
#    print(f"{dan} * {i} = {dan * i:2d})