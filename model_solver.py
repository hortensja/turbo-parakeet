import numpy as np
from scipy.integrate import odeint

from math_util import normalize_initial_conditions as nic, randomize_initial_conditions as ric
from models.ammoaab import Model as Sabr
from models.aitfbaae import Model as Sb1b2h
from parameters import Parameters

model_dict = {'SABR': Sabr, 'SBBH': Sb1b2h}


class ModelSolver:

    def __init__(self, model_type):
        self.model = model_dict[model_type]()
        self.delt = 0.01
        self.tmax = 10.0
        self._init_conds = ric()

    @property
    def init_conds(self):
        return self._init_conds

    @init_conds.setter
    def init_conds(self, conds):
         self._init_conds = nic(conds)

    def set_delt(self, delt):
        self.delt = delt

    def set_tmax(self, tmax):
        self.tmax = tmax


    def set_model(self, model):
        self.model = model

    def solve(self):
        t = np.arange(0, self.tmax, self.delt)
        y = odeint(self.model.get_set_of_ode, self._init_conds, t)
        x = np.linspace(0.0, self.tmax, len(y))
        return (x, y)

    def get_legend(self):
        return self.model.get_legend()

    def get_title(self):
        return self.model.get_title()

    def update_params(self, all_params):
        globals = all_params.get_globals()
        self.model.set_params(all_params.get_params())
        self.set_delt(globals['delt'])
        self.set_tmax(globals['tmax'])
        self._init_conds = nic(all_params.get_inits())

    def get_params(self):
        globals = {'delt': self.delt, 'tmax': self.tmax}
        return Parameters(self.model.get_legend(), self.model.get_params(), globals, self._init_conds)
