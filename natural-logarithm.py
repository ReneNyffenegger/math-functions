import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0.01, np.e**2 + 0.1, 100)
y = np.log(x)

plt.plot(x, y, label='log(x)')

def mark_coord(x, label, offset):
    y = np.log(x)
    plt.scatter(x, y, color='red')
    plt.annotate(label, (x, y), textcoords="offset points", xytext=offset   , ha='center', fontsize=8, color='red')


mark_coord(  1/np.e  , 'log(1/e)', ( 22, -7))
mark_coord(  1       , 'log(1)'  , ( 14,-10))
mark_coord(  np.e    , 'log(e)'  , (-10,  6))
mark_coord(  np.e**2 , 'log(e^2)', (-10,-11))

plt.xlabel('x')
plt.ylabel('log(x)')
plt.title('Natuaral logarithm')

plt.grid()
plt.savefig('img/natural-logarithm.png')
