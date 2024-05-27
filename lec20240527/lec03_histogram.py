import matplotlib.pyplot as plt
import numpy as np

def main():
    dices = np.random.randint(1, 7, size=100000) # random 모듈과 다름

    print(dices)

    plt.hist(dices, bins=6, color="b")
    plt.ylabel("Temperature(℃)")
    
    plt.legend()

    #plt.show()

    plt.savefig("./hist_temp.png")

if __name__ == "__main__":
    main()