
from matplotlib import pyplot as plt
'''
k = [i for i in range(5)]
pk = [0.1426, 0.2852, 0.2852, 0.19, 0.095]          # 1 задание
plt.bar(k, pk)
plt.title('График распределения')
plt.xlabel('k')
plt.ylabel('Pk')
plt.show()'''

import math
p0 = 0                                      # 2 задание
ro = 3
N = 7
for i in range(N + 1):
    p0 += ro ** i/math.factorial(i)
p0 += ro ** 8/math.factorial(7)/4
p0 = 1/p0
po4 = ro ** 8 * p0/math.factorial(7)/4
pzan = ro ** N/math.factorial(N - 1)/(N - ro)
Mtr = 0
for i in range(7):
    Mtr += ro ** i/math.factorial(i)
Mtr = Mtr * ro + ro ** (N+1)*(N + 1 - ro)/math.factorial(N - 1)/(N - ro) ** 2
Mtr = p0 * Mtr
Mo4 = ro ** (N + 1) * p0/math.factorial(N - 1)/(N - ro) ** 2
Msv = 0
for i in range(1, N + 1):
    Msv += i * ro ** i/math.factorial(N + i)
Msv *= p0
Mzan = 7 - Msv
Tozh = ro ** 7 * p0 / 0.119 / math.factorial(N - 1) / (N - ro) ** 2
Toozh = ro ** (N + 1) * p0 / math.factorial(N - 1) / (N - ro) ** 2
Ttr = Tozh + 1 / 0.119
print(Ttr)
k_new = [i for i in range(13)]
pk_new = list()
pk_new.append(p0)
for i in k_new:
    if i == 0:
        continue
    elif i <= 7:
        pki = ro ** i * pk_new[0] / math.factorial(i)
    else:
        pki = ro ** i * pk_new[0] / math.factorial(N) / N ** (i - N)
    pk_new.append(pki)

plt.bar(k_new, pk_new)
plt.title('График распределения вероятностей состояний')
plt.xlabel('k')
plt.ylabel('Pk')
plt.show()



