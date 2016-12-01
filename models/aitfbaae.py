from __future__ import division
from i_model import IModel


class Model(IModel):
    default_params = {'mu': 1/3, 'alpha': lambda x: 0.439, 'sigma': 0, 'gamma': 1.5, 'delta': 0.13, 'rho': 0.13, 'phi': 0.15}

    def __init__(self, params = default_params):
        self.params = params

    def set_params(self, new_params):
        self.params = new_params

    def update_param(self, param_name, param):
        try:
            self.params[param_name]
            self.params[param_name] = param
        except KeyError:
            print("Parameter doesn't exist")

        # y = [s b1 b2 h]

    def get_set_of_ode(self, y, t):
        p = self.params

        def dsdt(y, t):
            return (p['mu'] - (p['alpha'](p['sigma']))*y[0]*(y[1]+y[2]) - p['mu']*y[0])

        def db1dt(y, t):
            return ((p['alpha'](p['sigma']))*y[0]*(y[1]+y[2]) - (p['gamma']+p['mu'])*y[1])

        def db2dt(y, t):
            return (p['gamma']*y[1] - (p['mu']+p['rho']) * y[2] - p['sigma'] * y[2] * y[3] + p['phi']*y[3])

        def dhdt(y, t):
            return (p['rho'] * y[2] + p['delta'] * y[2] * y[3] - (p['phi'] + p['mu']) * y[3])

        return [dsdt(y,t), db1dt(y,t), db2dt(y,t), dhdt(y,t)]

    def get_legend(self):
        return ["S", "B1", "B2", "H"]
