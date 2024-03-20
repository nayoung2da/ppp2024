#1부터 n까지 짝수의 합은?
n = 250
total = 0

for i in range(n):
    i = i + 1
    if i % 2 == 0:
        total = total + i

print(f"1부터 {n}까지의 짝수의 합은 {total:,}입니다.")