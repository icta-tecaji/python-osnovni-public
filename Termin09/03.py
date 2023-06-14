import numpy as np
import matplotlib.pyplot as plt

# SCATTER PLOT
# n = 1024
# X = np.random.normal(0, 1, n)
# Y = np.random.normal(0, 1, n)
# T = np.arctan2(Y, X)

# plt.axes([0.025, 0.025, 0.95, 0.95])
# plt.scatter(X, Y, s=75, c=T, alpha=0.5)

# plt.xlim(-1.5, 1.5), plt.xticks([])
# plt.ylim(-1.5, 1.5), plt.yticks([])
# # savefig('../figures/scatter_ex.png',dpi=48)
# plt.show()


# STOLPIČNI GRAF
# n = 12
# X = np.arange(n)
# Y1 = (1 - X / float(n)) * np.random.uniform(0.5, 1.0, n)
# Y2 = (1 - X / float(n)) * np.random.uniform(0.5, 1.0, n)

# plt.axes([0.025, 0.025, 0.95, 0.95])
# plt.bar(X, +Y1, facecolor="#9999ff", edgecolor="white")
# plt.bar(X, -Y2, facecolor="#ff9999", edgecolor="white")

# for x, y in zip(X, Y1):
#     plt.text(x + 0.4, y + 0.05, "%.2f" % y, ha="center", va="bottom")

# for x, y in zip(X, Y2):
#     plt.text(x + 0.4, -y - 0.05, "%.2f" % y, ha="center", va="top")

# plt.xlim(-0.5, n), plt.xticks([])
# plt.ylim(-1.25, +1.25), plt.yticks([])

# plt.show()

# Pie chart
n = 20
Z = np.ones(n)
Z[-1] *= 2

plt.axes([0.025, 0.025, 0.95, 0.95])

plt.pie(Z, explode=Z * 0.05, colors=["%f" % (i / float(n)) for i in range(n)])
plt.gca().set_aspect("equal")
plt.xticks([]), plt.yticks([])

plt.show()
