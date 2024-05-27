import matplotlib.pyplot as plt
import numpy as np

def main():
    tmax = np.random.rand(30) * 15 + 15
    tmin = tmax - (np.random.rand(30) * 5 + 5)

    plt.plot(tmax, color="r", label="TMAX")
    plt.plot(tmin, color="b", label="TMIN")

    plt.ylabel("Temperature(℃)")
    
    plt.legend()
    # plt.show()
    plt.savefig("./line_temp.png")

if __name__ == "__main__":
    main()