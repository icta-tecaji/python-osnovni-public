# Matplotlib
import matplotlib.pyplot as plt

import math

x = [math.radians(r) for r in range(-180, 180)]

cos = [math.cos(i) for i in x]
sin = [math.sin(i) for i in x]

# for i, x_ in enumerate(x[::30]):
#     print(f"x: {x_:7.4f} \t sin: {sin[i]:7.4f}  \t cos: {cos[i]:7.4f}")

plt.figure(figsize=(8, 6))

a = plt.subplot(2, 2, 2)
a.plot(x, cos, color="red", linewidth=2, linestyle="--", label="cos")
a.plot(x, sin, color="lime", label="sin")
a.legend()

b = plt.subplot(2, 2, 3)
b.plot(x, sin, color="#00ff00")

plt.show()
