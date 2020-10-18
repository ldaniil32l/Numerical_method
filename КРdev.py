import matplotlib.pyplot as plt

# n - порядок разности
n = 4
# Список значений x лишь до 0.6
# из-за того, что график очень быстро растет
x = [-1, -0.8, -0.6, -0.4, -0.2, 0, 0.2, 0.4, 0.6]
# h - величина шага
h = (x[-1] - x[0]) / (len(x) - 1)

# В списки h и ans записаны значения функции 
ans = []
f = []
for i in x:
    ans.append(1 / (1 + (25 * i * i)))
for i in x:
    f.append(1 / (1 + (25 * i * i)))

# Получаем конечные разности
for i in range(n + 1):
    for j in range(n, i, -1):
        f[j] = f[j] - f[j - 1]

# Получаем значения интерполяционного полинома
a = []
for k in x:
    p = f[n]
    t = (k - x[0]) / h
    for i in range(n - 1, -1, -1):
        p = p*(t - i) / (i + 1) + f[i]
    a.append(p)

# Выводим графики
plt.plot(x, a)
plt.plot(x, ans)
plt.grid()
plt.xlabel('x')
plt.ylabel('y')
plt.show()