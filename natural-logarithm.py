import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0.01, np.e**2 + 0.1, 100)
y = np.log(x)

plt.plot(x, y, label='log(x)')


def mark_coord(x, label, offset):
    y = np.log(x)
    plt.scatter(x, y, color='red')
#   plt.annotate(label, (x, y), textcoords="offset points", xytext=( 14,-10), ha='center', fontsize=8, color='red')
    plt.annotate(label, (x, y), textcoords="offset points", xytext=offset   , ha='center', fontsize=8, color='red')


mark_coord(  1/np.e  , 'log(1/e)', ( 22, -7))
mark_coord(  1       , 'log(1)'  , ( 14,-10))
mark_coord(  np.e    , 'log(e)'  , (-10,  6))
mark_coord(  np.e**2 , 'log(e^2)', (-10,-11))

# Mark special points …
# plt.scatter(   1   , np.log(1      ), color='red')
# plt.scatter(np.e   , np.log(np.e   ), color='red')
# plt.scatter(np.e**2, np.log(np.e**2), color='red')
# 
# # … and annotate them
# plt.annotate('log(1/e)', (1/np.e  , np.log(1/np.e  )), textcoords="offset points", xytext=( 14,-10), ha='center', fontsize=8, color='red')
# plt.annotate('log(1)'  , (   1    , np.log(1       )), textcoords="offset points", xytext=( 14,-10), ha='center', fontsize=8, color='red')
# plt.annotate('log(e^1)', (np.e    , np.log(np.e    )), textcoords="offset points", xytext=(-10,  6), ha='center', fontsize=8, color='red')
# plt.annotate('log(e^2)', (np.e**2 , np.log(np.e**2 )), textcoords="offset points", xytext=(-10,-11), ha='center', fontsize=8, color='red')

plt.xlabel('x')
plt.ylabel('log(x)')
plt.title('Natuaral logarithm')

plt.grid()
# plt.show()
plt.savefig('img/natural-logarithm.png')
