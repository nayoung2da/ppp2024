import time

def main():
    #x = int(input())
    count = 5

    while True:
        print(f"카운트다운... {count}", end="\r")
        time.sleep(1)
        count -= 1
        if count <= 0:
            break
    
    print()
    print("붐붐붐붐 심장이 뛰네")

if __name__ == "__main__":
    main()