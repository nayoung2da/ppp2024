def read_tmax(filename):
    results = []
    with open(filename) as f:
        lines = f.readlines()
        for line in lines[1:]:
            tokens = line.split(",")
            tmax = float(tokens[3])
            results.append(tmax)
    return results

def read_tmin(filename):
    results = []
    with open(filename) as f:
        lines = f.readlines()
        for line in lines[1:]:
            tokens = line.split(",")
            tmin = float(tokens[5])
            results.append(tmin)
    return results

def read_weather(filename, col_idx):
    results = []
    with open(filename) as f:
        lines = f.readlines()
        for line in lines[1:]:
            tokens = line.split(",")
            tmin = float(tokens[col_idx])
            results.append(tmin)
    return results

def main():
    #tmax = read_tmax("lec20240408/weather(146)_2022-2022.csv")
    #tmin = read_tmin("lec20240408/weather(146)_2022-2022.csv")

    tmax = read_weather("lec20240408/weather(146)_2022-2022.csv", 3)
    tmin = read_weather("lec20240408/weather(146)_2022-2022.csv", 5)

    print(f"연 최고 온도(max(tmax))는 {max(tmax):.1f}입니다.")
    print(f"연 최저 온도(min(tmin))는 {min(tmin):.1f}입니다.")

if __name__ == "__main__":
    main()