import time

def main():
    count = int(input("몇 초를 카운트하시겠습니까? : "))

    while True:
        print(f"카운트다운... {count}", end="\r")
        time.sleep(1)
        count -= 1
        if count <= 0:
            break

    print()
    print("펑~~")


if __name__ == "__main__":
    main()