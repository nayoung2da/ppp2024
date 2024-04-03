def text2list(nums):
    list = []
    tokens = nums.split(" ")
    for token in tokens:
        list.append(int(token))
    return list

def average(nums):
    return sum(nums)/len(nums)

def median(nums): 
    sorted_nums = sorted(nums)
    return sorted_nums[len(nums)//2]


#def read_file(filename):
        #with open(filename) as f:
        #    text = f.readline().strip()
         #   print(f"!{text}!")
          #  return text

def read_list_from_file(filename):
    data = []
    with open(filename) as f:
        lines = f.readlines()
        for line in lines:
            text = line.strip()
            print(f"!{line}!")
            nums = int(text)
            data.append(nums)
    #return " ".join(data)
    return data
    
def main():
    #input_text = read_file_multiline("lec20240403/numbers2.text")
    #nums = text2list(input_text)

    nums = read_list_from_file("lec20240403/numbers2.text")

    print("주어진 리스트는", nums)
    print("평균값은 {:.1f}".format(average(nums)))
    print("중앙값은 {}".format(median(nums)))
    print(f"최솟값은 {min(nums)}")
    print(f"최댓값은 {max(nums)}")
    print(f"리스트의 마지막 값은 {nums[-1]}")

if __name__ == "__main__":
    main()