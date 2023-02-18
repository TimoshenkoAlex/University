import numpy as np
import matplotlib.pyplot as plt
# 2 вариант: 9 строка

p0 = 101325
tao = 0.0065
T0 = 288
R = 29.27
t = [i for i in range(100)]
V_y = [30 * np.sin((2 * np.pi * time) / 100) for time in t]
H = [10950]
p = [p0 * (1 - (tao * H[0]) / T0) ** (1 / (tao * R))]
H_new = []
for i in range(1, 100):
    H.append(H[i - 1] + V_y[i])
    if H[i] <= 11000:
        pt = p0 * (1 - (tao * H[i]) / T0) ** (1 / (tao * R))
        p.append(pt)
    else:
        pt = 22610 * np.exp(-((H[i] - 11000) / (R * 216.5)))
        p.append(pt)

for i in range(100):
    if p[i] >= 22610:
        pt_new = (1 - (p[i] / p0) ** (tao * R)) * T0 / tao
        H_new.append(pt_new)
    else:
        pt_new = 11000 + R * 216.5 * np.log(22610 / p[i])
        H_new.append(pt_new)

plt.plot(t, H, '--o', color='blue')
plt.plot(t, H_new, ':2', color='red')
plt.show()
plt.plot(t, V_y)
plt.show()
plt.plot(t, p)
plt.show()
