import matplotlib.pyplot as plt
import numpy as np

def main():
    np.random.seed(0) #시드넘버를 잡아주면 매번 같은 그래프? => 1,2,3,...등등 

    n = 50
    x = np.random.rand(n)
    y = np.random.rand(n)

    plt.scatter(x, y)
    plt.savefig("./scatter.png")

if __name__ == "__main__":
    main()