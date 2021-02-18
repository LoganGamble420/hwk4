import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import interp1d

def f(x):
    return np.sqrt(x) + np.cos(x)

x_range = np.arange(0,4*np.pi,0.8)
x_f_range = np.arange(0,4*np.pi, 0.01)

def df(x):
    return 0.5 * np.sqrt(x) - np.sin(x)

inter = interp1d(x_range,f(x_range), kind = 'linear')

inter2 = interp1d(x_range,f(x_range), kind = 'cubic' )

inter_fine = interp1d(x_f_range, df(x_f_range), kind = 'linear')

inter_fine2 = interp1d(x_f_range, df(x_f_range), kind = 'cubic')

plt.plot(x_f_range, f(x_f_range), 'o' , x_range, inter(x_range), '-' ,
        x_range, inter2(x_range), '--', x_f_range, df(x_f_range), '.',
        x_range, df(inter_fine(x_range)), 'd',
        x_range, df(inter_fine2(x_range)),'*')
plt.legend(['true data','linear','cubic', 'true deriv', 'linear derived', 'cubic derived'], loc='best')
plt.show()

