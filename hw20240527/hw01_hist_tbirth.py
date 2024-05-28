import os
import requests
import matplotlib.pyplot as plt

url = "https://api.taegon.kr/stations/146/?sy=1980&ey=2023&format=csv"
filename = "weather_146_1980-2023.csv"

if not os.path.exists(filename):
    with open(filename, "w", encoding="utf-8") as f:
        res = requests.get(url)
        f.write(res.text)

def read_tbirth(filename):
    result = []
    with open(filename, encoding="utf-8-sig") as f:
        lines = f.readlines()
        for line in lines[1:]:
            token = line.strip().split(",")
            if token[0].strip() >= '2004' and token[1].strip() == '8' and token[2].strip() == '14':
                tbirth = float(token[4].strip())
                result.append(tbirth)
    return result

def main():
    tbirth = read_tbirth(filename)
    print(f"내 생일 기온들: {tbirth}")
    
    plt.hist(tbirth, bins=10, color="y")
    plt.title("Temperature on Nayeong's birthday")
    plt.xlabel("Temperature(℃)")
    plt.ylabel("How many?")

    plt.savefig("hw20240527/hw01_hist_tbirth.png")


if __name__ == "__main__":
    main()

