x = int(input("x좌표를 입력하시오. :"))
y = int(input("y좌표를 입력하시오. :"))

if x > 0 and y > 0:
    print("점 ({}, {})는 1사분면입니다.".format(x, y))
elif x < 0 and y > 0:
    print("점 ({}, {})는 2사분면입니다.".format(x, y))
elif x < 0 and y < 0:
    print("점 ({}, {})는 3사분면입니다.".format(x, y))
elif x > 0 and y < 0:
    print("점 ({}, {})는 4사분면입니다.".format(x, y))
elif x == 0:
    print("y축 위의 점입니다.")
else:
    print("x축 위의 점입니다.")