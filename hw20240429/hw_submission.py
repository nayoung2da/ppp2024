import requests

def submit(name: str, t_max: float, t_max_date: str, gap_max: float, gap_max_date: str) -> None:
    URL = "https://script.google.com/macros/s/AKfycbybB2LSi0F85FkC4KmI0XgjMqvhn7-6eJjZQi0oucbgbEvwDmNVRoyMMnd5UyezpqJp/exec"
    PARAMS = {
        '제출자': name,
        '최대기온': t_max,
        '최대기온날짜': t_max_date,
        '최대일교차': gap_max,
        '최대일교차날짜': gap_max_date,
    }

    # sending get request and saving the response as response object
    r = requests.get(url=URL, params=PARAMS)
    if r.status_code != 200:
        print("과제가 정상적으로 제출되지 않았습니다.")