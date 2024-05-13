def get_numbers():
    results = []
    while True:
        try:
            x = input("X=>?")
            num = int(x)
            if num == -1:
                return results
                #break
            if num < 0:
                continue
            results.append(num)
        except ValueError:
            print(f"입력한 {x}는 저장되지 않습니다.")

def avg(nums):
    if len(nums) != 0:
        return sum(nums)/len(nums)
    return None

def main():
    numbers = get_numbers()
    print(f"입력받은 숫자는 {numbers}, 갯수는 {len(numbers)}, 평균은 {avg(numbers)}")

if __name__ == "__main__":
    main()