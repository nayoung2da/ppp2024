def text2list(nums):
    list = []
    split_num = nums.split(" ")
    for i in split_num:
        list.append(int(i))
    return list

def average(nums):
    return sum(nums)/len(nums)

def median(nums): 
    sorted_nums = sorted(nums)
    n = len(nums)
    if n % 2 == 0:
        median1 = (sorted_nums[n//2])
        median2 = (sorted_nums[n//2 - 1])
        if median1 > median2:
            return median1
        else:
            return median2
    else:
        return sorted_nums[n//2]

def main():
    input_text = "5 10 3 4 7"
    nums = text2list(input_text)
    print("주어진 리스트는", nums)
    print("평균값은 {:.1f}".format(average(nums)))
    print("중앙값은 {}".format(median(nums)))
    print(f"최솟값은 {min(nums)}")
    print(f"최댓값은 {max(nums)}")

if __name__ == "__main__":
    main()