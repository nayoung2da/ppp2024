def read_col(filename, col_name):
    dataset = []
    with open(filename) as f:
        lines = f.readlines()
        header = [x.strip() for x in lines[0].split(",")]
        print(header)
        col_idx = header.index(col_name)
        print(col_name, col_idx)
        for line in lines[1:]:
            tokens = line.split(",")
            dataset.append(float(tokens[col_idx]))
    return dataset

def count_rainday(rainfall):
    rain_day = 0
    for rain in rainfall:
        if rain >= 5:
            rain_day += 1
    return rain_day

def longest_rainday(rainfall):
    rain_event = []

    prev_rain_count = 0
    for rain in rainfall:
        if rain == 0:
            if prev_rain_count > 0:
                rain_event.append(prev_rain_count)
            prev_rain_count = 0
        else:
            prev_rain_count += 1
    return max(rain_event)

#def longest_rainday(rainfall):
#    max_con_rainday = 0
#    corrent_con_raindat = 0
#    for rain in rainfall:
#        if rain > 0:
#            corrent_con_raindat += 1
#        else:
#            max_con_rainday = max(max_con_rainday, corrent_con_raindat)
#            corrent_con_raindat = 0
#    max_con_rainday = max(max_con_rainday, corrent_con_raindat)
#
#    return max_con_rainday

def max_rainfall_event(rainfall):
    rain_event = []

    prev_rain_count = 0
    prev_rain = 0

    for rain in rainfall:
        if rain == 0:
            if prev_rain_count > 0:
                rain_event.append(prev_rain)
            prev_rain_count = 0
            prev_rain = 0
        else:
            prev_rain_count += 1
            prev_rain += rain
    return max(rain_event)

def top_rank(values, limit):
    #return sorted(values, reverse=True)[:limit] #교수님꺼 reverse 사용
    #return sorted(values)[-limit:] 3등->2등->1등으로 뽑음
    return sorted(values)[-limit:][::-1] #2번째꺼 고친거~

def read_col_int(filename, col_name):
    dataset = []
    with open(filename) as f:
        lines = f.readlines()
        header = [x.strip() for x in lines[0].split(",")]
        print(header)
        col_idx = header.index(col_name)
        print(col_name, col_idx)
        for line in lines[1:]:
            tokens = line.split(",")
            dataset.append(int(tokens[col_idx]))
    return dataset

def sumifs(rainfall, months, condition):
    total = 0
    for i in range(len(rainfall)):
        rain = rainfall[i]
        month = months[i]
    if month in condition:
        total += rain
    return total

def get_data_ifs(values, conditions, criteria):
    dataset = []
    for rain, year in zip(values, conditions):
        if year == criteria:
            dataset.append(rain)
    return dataset

def read_col_year(weather_filename_2021, col_name, year):
    dataset = []
    with open(weather_filename_2021) as f:
        lines = f.readlines()
        header = [x.strip() for x in lines[0].split(",")]
        col_idx = header.index(col_name)
        print(col_name, col_idx)
        for line in lines[1:]:
            tokens = line.split(",")
            y = int(tokens[0])
            if y == year:
                dataset.append(float(tokens[col_idx]))
    return dataset

def main():
    weather_filename = "lec20240415/weather(146)_2022-2022.csv"
    weather_filename_2021 = "lec20240415/weather(146)_2001-2022.csv"
    tavg = read_col(weather_filename, "tavg")
    tmax = read_col(weather_filename, "tmax")
    rainfall = read_col(weather_filename, "rainfall")
    months_float = read_col(weather_filename, "month")
    months = [int(x) for x in months_float]
    months = read_col_int(weather_filename, "month")
    print(months)
    print(tavg)
    #1번 평균 기온
    print(f"연 평균 기온은 {sum(tavg)/len(tavg):.2f}C입니다.")
    #2번 5mm이상 강우일수
    print(f"5mm 이상 강우일수는 {count_rainday(rainfall)}일입니다.")
    #3번 총 강우량
    print(f"총 강우량은 {sum(rainfall):.1f}mm입니다.")
    #4번 최장연속강우일수
    print(f"최장연속 강우일수는 {longest_rainday(rainfall)}일입니다.")
    #5번 강우이벤트 중 최대 강우량
    print(f"강우이벤트 중 최대 강우량은 {max_rainfall_event(rainfall):.1f}mm입니다.")
    #6번 가장 더운 날 top3
    print(f"가장 더운 날 top3는 {top_rank(tmax, 3)}C입니다.")

    #7번 6, 7, 8월강수량
    print(f"여름철 강수량은 {sumifs(rainfall, months, [6, 7, 8])}mm입니다.")
    #8번 2021, 2022년 총 강수량
    rainfall_all = read_col(weather_filename_2021, "rainfall")
    year_all = read_col_int(weather_filename_2021, "year")
    rainfall_2021 = get_data_ifs(rainfall_all, year_all, 2021)
    print(f"총 강수량은 {sum(rainfall_2021):.1f}mm입니다.")

    rainfall_2021 = read_col_year(weather_filename_2021, "rainfall", 2021)
    print(f"총 강수량은 {sum(rainfall_2021):.1f}mm입니다.")

if __name__ == "__main__":
    main()