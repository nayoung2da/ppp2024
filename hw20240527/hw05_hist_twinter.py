import os
import requests
import matplotlib.pyplot as plt

url = "https://api.taegon.kr/stations/146/?sy=1980&ey=2023&format=csv"
filename = "weather_146_1980-2023.csv"

if not os.path.exists(filename):
    with open(filename, "w", encoding="utf-8") as f:
        res = requests.get(url)
        f.write(res.text)

def read_twinter(filename):
    result = []
    with open(filename, encoding="utf-8-sig") as f:
        lines = f.readlines()
        for line in lines[1:]:
            token = line.strip().split(",")
            if '1' <= token[1].strip() <= '2' or token[1].strip() == '12':
                twinter = float(token[4].strip())
                result.append(twinter)
    return result

def main():
    twinter = read_twinter(filename)
    
    plt.hist(twinter, bins=10, color="pink")
    plt.title("Temperature on Jeonju's Winter")
    plt.xlabel("Temperature(℃)")
    plt.ylabel("How many?")
    

    plt.savefig("hw20240527/hw05_hist_twinter.png")


if __name__ == "__main__":
    main()