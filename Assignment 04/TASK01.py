import numpy as np
import matplotlib.pyplot as plt


n_values = [500, 1000, 2000, 5000, 10000, 15000, 20000, 50000, 100000]

for n in n_values:

    dice1 = np.random.randint(1, 7, n)
    dice2 = np.random.randint(1, 7, n)
    s = dice1 + dice2


    h, h2 = np.histogram(s, range(2, 14))


    plt.bar(h2[:-1], h / n, width=0.8, alpha=0.7, color='blue', edgecolor='black')
    plt.title(f"The value of n = {n}")
    plt.xlabel("Sum of two dice")
    plt.show()


