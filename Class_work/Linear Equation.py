import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0, 20, 7)

y1 = 1 + 2*x
y2 = 1 + 3*x
y3 = 1 + 4*x

plt.plot(x, y1, 'r:', label="1+ 2x")
plt.plot(x, y2, 'b--', label="1 + 3x")
plt.plot(x, y3, 'g-', label="1 + 4x")

plt.title("Showing the Linear equation.")
plt.xlabel("x")
plt.ylabel("y")
plt.legend()
plt.grid(True)
plt.show()