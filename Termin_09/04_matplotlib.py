from msilib.schema import AdvtExecuteSequence
import matplotlib.pyplot as plt
import math 

x = [math.radians(x) for x in range(-180, 180)]
print(x)

cos = [math.cos(i) for i in x]
sin = [math.sin(i) for i in x]
# --------------------------------------------------------

plt.figure(figsize=(8,6), dpi=100)

# a = plt.subplot(2, 2, 2)

# a.plot(x, cos)
# a.plot(x, sin)

# b = plt.subplot(2, 2, 3)
# b.plot(x, cos)
# b.plot(x, sin)

plt.plot(x, cos, color="blue", linewidth=1, linestyle="-")
plt.plot(x, sin, color="red", linewidth=0.5, linestyle="--")

plt.xlim(-5, max(x))
plt.xticks([-3.14, -3.14/2, 0, 3.14/2, 3.14], [r"$-\pi$", r"$-\pi/2$", "nula", "pi polovic", "pi"])
plt.ylim(min(cos), 4)
plt.grid()

ax = plt.gca()
ax.spines['right'].set_color('none')

plt.show()
