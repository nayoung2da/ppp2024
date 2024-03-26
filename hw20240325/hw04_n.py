def sum_n(n):
    total = 0
    for i in range(n):
        i = i + 1
        total = total + i
    print(f"1부터 {n}까지의 합은 {total:,}입니다.")

def main():
    n = int(input("1부터 n까지의 합을 구할 때, n의 값을 구하시오. : "))
    sum_n(n)

if __name__=="__main__":
    main()