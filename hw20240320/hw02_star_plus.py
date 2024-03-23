#별찍기
n = int(input("출력할 줄의 수를 입력해주세요. : "))

#왼쪽 정렬 삼각형 별
print("="*5, "왼쪽 정렬 삼각형 별입니다", "="*5)
for i in range(n):
    i = i + 1
    print("*" * i)

#오른쪽 정렬 삼각형 별
print("="*5, "오른쪽 정렬 삼각형 별입니다", "="*5)
for i in range(n):
    i = i + 1
    print(" " * (n - i), end="")
    print("*" * i)

#정삼각형 별
print("="*5, "정삼각형 별입니다", "="*5)
for i in range(n):
    i = i + 1
    print(' ' * (n - i), end = '')
    print('*' * (2 * i - 1))