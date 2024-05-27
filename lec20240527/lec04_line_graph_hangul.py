#한글이 안나오는 이유 : 폰트 지정이 되어 있지 않아서잉

import matplotlib.pyplot as plt
import numpy as np

def main():
    plt.rcParams['font.family'] = ['NanumGothic', 'sans-serif']
    plt.rcParams['axes.unicode_minus'] = False

    tmax = np.random.rand(30) * 15 + 15
    tmin = tmax - (np.random.rand(30) * 5 + 5)

    plt.plot(tmax, color="r", label="최고기온")
    plt.plot(tmin, color="b", label="최저기온")

    plt.ylabel("기온(℃)")
    
    plt.legend()
    plt.savefig("./line_temp_hangul.png")

if __name__ == "__main__":
    main()