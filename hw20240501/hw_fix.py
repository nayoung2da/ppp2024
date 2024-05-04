import sys
if "./" not in sys.path:
    sys.path.append("./")
import os
import requests
from hw20240501 import hw_submission

def read_date(weather_filename):
    dataset = []
    with open(weather_filename, encoding="utf-8-sig") as f:
        lines = f.readlines()
        for line in lines[8:]:
            tokens = line.strip().split(",")
            if len(tokens) < 5:
                continue
            date = tokens[0].strip() if tokens[0].strip() != '' else None
            locate = tokens[1].strip() if tokens[1].strip() != '' else None
            temp_value = float(tokens[3].strip()) if tokens[3].strip() != '' else None
            precip_value = float(tokens[4].strip()) if tokens[4].strip() != '' else None
            dataset.append((date, locate, temp_value, precip_value))
    return dataset


def read_tmax(data):
    tmax_date = None
    tmax_value = float("-inf")
    for date, locate, temp_value, precip_value in data:
        if temp_value is None:
            continue
        if temp_value > tmax_value:
            tmax_date = date
            tmax_value = temp_value
    return tmax_date, tmax_value

def read_tdiff(data):
    tdiff_date = None
    tdiff_value = float("-inf")
    for date, locate, temp_value, precip_value in data:
        if temp_value is None or precip_value is None:
            continue
        temp_diff = temp_value - precip_value
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