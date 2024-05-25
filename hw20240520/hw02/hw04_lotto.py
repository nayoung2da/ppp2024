import random

def get_lotto():
    results = []

    while True:
        num = random.randint(1, 45)
        if num not in results:
            results.append(num)
        if len(results)==6:
            return sorted(results)

def main():
    count = int(input('로또 몇 장을 뽑으시겠습니까? : '))

    for i in range(count):
        lotto_nums = get_lotto()
        print(f"{i+1} : {lotto_nums}")

if __name__ == "__main__":
    main()