import numpy as np
import matplotlib.pyplot as plt

def logit(p):
    return np.log(p / (1 - p))

p_values = np.linspace(0.0001, 0.9999, 500)

y_values = logit(p_values)

plt.plot(p_values, y_values, label='Logit function')
plt.xlabel('p (Probability)')
plt.ylabel('logit(p)')

plt.title('Logit function')

plt.grid()
plt.legend()

# plt.show()
plt.savefig('img/logit.png')
