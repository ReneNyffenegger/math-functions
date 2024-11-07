import numpy as np
import matplotlib.pyplot as plt

def standard_logistic(x):
    return 1 / (1 + np.exp(-x))

x_values = np.linspace(-10, 10, 400)

y_values = standard_logistic(x_values)

plt.plot(x_values, y_values, label='Logistic Function')
plt.xlabel('x')
plt.ylabel('f(x)')

plt.title("Logistic Function")

plt.grid()
plt.legend()

# plt.show()
plt.savefig('img/standard-logistic-function.png')
