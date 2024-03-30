def average(nums):
    avg = sum(nums) / len(nums)
    return avg

def main():
    nums = [3, 5, 2, 6]
    print(f"숫자 리스트의 평균값은 {average(nums)}입니다.")

if __name__=="__main__":
    main()