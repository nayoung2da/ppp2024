def largest(nums):
    largest_num = nums[0]
    for num in nums:
        if largest_num < num:
            largest_num = num
    return largest_num

def main():
    x = [3, 7, 5, 8, 2, 3]
    print(f"가장 큰 수는 {largest(x)}입니다.")

if __name__ == "__main__":
    main()