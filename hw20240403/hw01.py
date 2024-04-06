def count(nums):
    return len(nums)

def average(nums):
    return sum(nums)/len(nums)

def median(nums): 
    sorted_nums = sorted(nums)
    return sorted_nums[len(nums)//2]

def read_list_from_file(filename):
    data = []
    with open(filename) as f:
        lines = f.readlines()
        for line in lines:
            text = line.strip()
            print(f"!{line}!")
            nums = int(text)
            data.append(nums)
    return data
    
def main():
    nums = read_list_from_file("hw20240403/numbers1.text")

    print("주어진 파일의 개수는 {}".format(count(nums)))
    print("평균값은 {:.1f}".format(average(nums)))
    print(f"최댓값은 {max(nums)}")
    print(f"최솟값은 {min(nums)}")
    print("중앙값은 {}".format(median(nums)))

if __name__ == "__main__":
    main()