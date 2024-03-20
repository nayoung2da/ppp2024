#1부터 100까지 합을 구하시오.
total = 0

for i in range(100):
    i = i + 1
    total = total + i

print(f"1부터 100까지의 합은 {total}입니다.")

#1부터 n까지 합을 구하시오.
n = 250
total = 0

for i in range(n):
    i = i + 1
    total = total + i

print(f"1부터 {n}까지의 합은 {total:,}입니다.")