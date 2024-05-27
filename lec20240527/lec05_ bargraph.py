import matplotlib.pyplot as plt
import numpy as np

def main():
    plt.rcParams['font.family'] = ['NanumGothic', 'sans-serif']
    plt.rcParams['axes.unicode_minus'] = False

    fig, ax = plt.subplots(figsize=(15, 6))

    year = [str(x+2001) for x in range(20)]
    rain = np.random.rand(20) * 200 + 1000

    ax.bar(year, rain, color="y")

    ax.set_ylabel("연평균강우량(mm)")
    ax.set_xlabel("년도")

    fig.savefig("./bar_rain.png")

if __name__ == "__main__":
    main()

#막대는 온도 그리면 안됨.. 막대의 2배가 그 양이 2배인 경우..?에 사용
#ax plt 차이 는 아직은 몰라도됑 ..~~ 근데 ax가 사이즈 지정도 가능하고 그래프 여러개 그릴 수 있는 듯