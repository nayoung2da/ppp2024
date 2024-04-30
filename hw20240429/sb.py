import os
import requests
import hw_submission

def read_date(weather_filename):
    dataset = []
    with open(weather_filename) as f:
        lines = f.readlines()
        for line in lines[8:]:
            tokens = line.split(",")
            date, locate = tokens[:2]
            dataset.append((date, locate, float(tokens[3]), float(tokens[4])))
    return dataset

def read_tmax(data):
    tmax_date = None
    tmax_value = float("-inf")
    for date, value in data:
        if value[3] is None:
            continue
        if float(value[3]) > tmax_value:
            tmax_date = date
            tmax_value = float(value[3])
    return tmax_date, tmax_value

def read_tdiff(data):
    tdiff_date = None
    tdiff_value = float("-inf")
    for date, value in data:
        if value[2] is None or value[3] is None:
            continue
        temp_diff = float(value[3]) - float(value[2])
        if temp_diff > tdiff_value:
            tdiff_date = date
            tdiff_value = temp_diff
    return tdiff_date, tdiff_value

def main():
    filename = "ta_20240429021144.csv"
    URL = f"https://data.kma.go.kr/stcs/grnd/downloadGrndTaList.do?fileType=csv&pgmNo=70&menuNo=432&serviceSe=F00101&stdrMg=99999&startDt=19040101&endDt=20240422&taElement=MIN&taElement=AVG&taElement=MAX&stnGroupSns=&selectType=1&mddlClssCd=SFC01&dataFormCd=F00501&dataTypeCd=standard&startDay=19040101&startYear=1904&endDay=20240422&endYear=2024&startMonth=01&endMonth=12&sesnCd=0&txtStnNm=%EC%A0%84%EC%A3%BC&stnId=146&areaId=&gFontSize="

    if not os.path.exists(filename):
        with open(filename, "w") as f:
            res = requests.get(URL)
            f.write(res.text)

    data = read_date(filename)

    tmax_date, tmax_value = read_tmax(data)
    tdiff_date, tdiff_value = read_tdiff(data)

    hw_submission.submit("우나영", tmax_value, tmax_date, tdiff_value, tdiff_date)

if __name__ == "__main__":
    main()