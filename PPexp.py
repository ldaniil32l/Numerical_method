import matplotlib.pyplot as plt
from math import exp

# n - порядок разделенной разности
n = 5
#Значения, по которым будут построены графики
x = [0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1]
#Список, в который будут записаны значения функции экспоненты
exp_list = []
for i in x:
    exp_list.append(exp(i))

#Во внешнем цикле строятся полиномы с разными порядка разд. разности.
for k in range (n):
#   В f записываем занчения функции экспоненты
    f = []
    for i in x:
        f.append(exp(i))
#   В f записываем р.р.
    for i in range(k):
        for j in range (len(x) - 1, i, -1):
            f[j] = (f[j] - f[j - 1])/(x[j] - x[j - i - 1])
#   Находим значения интерполяционного полинома
    a = []
    for t in x:
        p = f[len(x) - 1]
        for i in range (len(x) - 1, -1, -1):
            p = p * (t - x[i]) + f[i]
        a.append(p)
#   Строим график для соответствующего порядка р.р.
    plt.plot(x, a)
#Строим график экспоненты
plt.plot(x, exp_list)
plt.grid()
plt.xlabel('x')
plt.ylabel('y')
plt.show()