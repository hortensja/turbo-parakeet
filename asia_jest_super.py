import numpy as np
from scipy.integrate import odeint

import matplotlib.pyplot as mp
from sklearn.preprocessing import label

from math_util import normalize_initial_conditions as nic
from models.ammoaab import Model as sabr
from models.aitfbaae import Model as sb1b2h

if __name__ == "__main__":
    #model = sabr()
    model = sb1b2h()

    i = lambda x: x
    print(i(5))

    y0 = [3,2,1,2]
    y0 = nic(y0)
    print(y0)

    tmax = 4.0
    t = np.arange(0, tmax, 0.01)
    #print(t)


    print(model.get_legend())

    print(unichr(500))

    y = odeint(model.get_set_of_ode, y0, t)
    print(y)
    x = np.linspace(0.0, tmax, len(y))
    plt = mp.plot(x, y, label='')
    mp.legend(plt, model.get_legend())
    mp.show()
