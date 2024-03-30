def get_range_list(n):
    return list(range(1, n+1))

def main():
    n = int(input("1부터 n까지 리스트를 작성합니다. n의 값을 입력해주세요. : "))
    print("="*12, f"1부터 {n}까지 리스트", "="*12)
    print(f"{get_range_list(n)}")

if __name__ == "__main__":
    main()