import matplotlib
import numpy as np
import matplotlib.pyplot as plt

from math import *
#Рациональное параметрическое представление строфоиды u = tg(φ):
#x=a*(t**2-1)(t**2+1)
#y=at(t**2-1)(t**2+1)

t = np.linspace(-2, 2, 2000)
all_a = [2, 5]                                 # набор а

for a in all_a:
    x = a * (t * t - 1) / (t * t + 1)
    y = a * t * (t * t - 1) / (t * t + 1)
    plt.plot(x, y, label="a = {}".format(a))


plt.plot([0 for i in y], 2 * y, color="black")  # ось X
plt.plot(2 * x, [0 for i in x], color="black")  # ось Y
plt.grid()                                      # сетка
plt.legend(shadow=True)                         # легенда
plt.show()
