import numpy as np
from scipy.integrate import odeint

import matplotlib.pyplot as mp

from math_util import normalize_initial_conditions as nic, randomize_initial_conditions as ric
from models.ammoaab import Model as sabr
from models.aitfbaae import Model as sb1b2h

model_dict = {'SABR':sabr, 'SBBH':sb1b2h}

class ModelSolver:

    def __init__(self, modelType):
        self.model = model_dict[modelType]()
        self.delt = 0.01
        self.tmax = 10.0
        self.randomize_init_conds()

    def set_delt(self, delt):
        self.delt = delt

    def set_tmax(self, tmax):
        self.tmax = tmax

    def set_init_conds(self, conds):
         self.init_conds = nic(conds)

    def set_model(self, model):
        self.model = model

    def randomize_init_conds(self):
        self.init_conds = ric()
        print(self.init_conds)

    def solve(self):
        t = np.arange(0, self.tmax, self.delt)
        y = odeint(self.model.get_set_of_ode, self.init_conds, t)
        x = np.linspace(0.0, self.tmax, len(y))
        return (x, y)

    def get_legend(self):
        return self.model.get_legend()

if __name__ == "__main__":

    model_solver = ModelSolver('SABR')
    #print(model_solver.solve())
    x, y = model_solver.solve()
    #print(x)
    plt = mp.plot(x, y, label='')
    mp.legend(plt, model_solver.model.get_legend())
    mp.show()
    #
    # print(model.get_legend())


