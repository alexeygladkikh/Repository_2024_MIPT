import matpotlib.pyplot as plt
import numpy as np

size = 10000

x = np.linspace(0, size, size)
y = np.random.normal(0, 1, size)

plt.plot(x, y)
plt.show()