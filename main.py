import random
import math
import matplotlib.pyplot as plt
N = 100

time = [i for i in range(N)]

a = [[0] * 3 for i in range(5)]
t = [[0] * 3 for i in range(5)]
p = [[0] * 3 for i in range(5)]
for i in range(5):
    for j in range(3):
        a[i][j] = random.uniform(10, 100)
        p[i][j] = random.uniform(1.3, 9.5)
        t[i][j] = random.uniform(5, 100)

y = [[0] * N for i in range(5)]
s = [0] * N

for j in range(5):
    for i in range(N):
        for k in range(3):
            y[j][i] += a[j][k] * math.exp(-(((i-t[j][k]) / p[j][k]) ** 2))
        s[i] += y[j][i]

for i in range(5):
    name = "Деталь" + str(i + 1)
    plt.title(name) # заголовок
    plt.xlabel("t") # ось абсцисс
    plt.ylabel("y") # ось ординат
    plt.grid()      # включение отображение сетки
    plt.plot(time, y[i])  # построение графика
    plt.show()

plt.title("Сумма") # заголовок
plt.xlabel("t") # ось абсцисс
plt.ylabel("y") # ось ординат
plt.grid()      # включение отображение сетки
plt.plot(time, s)  # построение графика
plt.show()
