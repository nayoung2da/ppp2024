import random

def get_lotto():
    results = []

    while True:
        num = random.randint(1, 45)
        if num not in results:
            results.append(num)
        if len(results)==6:
            #return results.sort()  불가능
            return sorted(results)
    #return [3, 5, 8, 10, 12, 15]

def main():
    count = 5

    for i in range(count):
        lotto_nums = get_lotto()
        print(f"{i+1} : {lotto_nums}")

if __name__ == "__main__":
    main()