import os
import requests
import matplotlib.pyplot as plt

url = "https://api.taegon.kr/stations/146/?sy=1980&ey=2023&format=csv"
filename = "weather_146_1980-2023.csv"

if not os.path.exists(filename):
    with open(filename, "w", encoding="utf-8") as f:
        res = requests.get(url)
        f.write(res.text)

def read_tsummer(filename):
    result = []
    with open(filename, encoding="utf-8-sig") as f:
        lines = f.readlines()
        for line in lines[1:]:
            token = line.strip().split(",")
            if '6' <= token[1].strip() <= '8':
                tsummer = float(token[4].strip())
                result.append(tsummer)
    return result

def main():
    tsummer = read_tsummer(filename)
    
    plt.hist(tsummer, bins=10, color="g")
    plt.title("Temperature on Jeonju's Summer")
    plt.xlabel("Temperature(℃)")
    plt.ylabel("How many?")

    plt.savefig("hw20240527/hw04_hist_tsummer.png")


if __name__ == "__main__":
    main()