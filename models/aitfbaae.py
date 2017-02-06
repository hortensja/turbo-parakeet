from __future__ import division

from math import sqrt

from i_model import IModel


class Model(IModel):
    default_params = {'mu': 0.333, 'alpha': 'lambda x: 0.439', 'sigma': 0, 'gamma': 1.5, 'delta': 0.13, 'rho': 0.13, 'phi': 0.15}

    def __init__(self, params=default_params):
        self.params = params

        # y = [s b1 b2 h]

    def get_set_of_ode(self, y, t):
        p = self.params

        alpha = eval(p['alpha'])

        def dsdt(y, t):
            return (p['mu'] - (alpha(p['sigma']))*y[0]*(y[1]+y[2]) - p['mu']*y[0])

        def db1dt(y, t):
            return (alpha(p['sigma'])*y[0]*(y[1]+y[2]) - (p['gamma']+p['mu'])*y[1])

        def db2dt(y, t):
            return (p['gamma']*y[1] - (p['mu']+p['rho']) * y[2] - p['sigma'] * y[2] * y[3] + p['phi']*y[3])

        def dhdt(y, t):
            return (p['rho'] * y[2] + p['delta'] * y[2] * y[3] - (p['phi'] + p['mu']) * y[3])

        return [dsdt(y, t), db1dt(y, t), db2dt(y, t), dhdt(y, t)]

    def get_legend(self):
        return ["S", "B1", "B2", "H"]

    def get_title(self):
        return "SB1B2H"

    def get_Rs(self):
        p = self.params
        alpha = eval(p['alpha'])

        rs1 = (alpha(p['sigma']))/(p['mu']+p['gamma'])
        rs2 = (p['phi']*p['rho'])/((p['mu']+p['phi'])*(p['mu']+p['rho']))
        r12 = (p['gamma'])/(p['mu']+p['rho'])
        sq = rs1 + sqrt(rs1*r12)
        b2max =(p['mu']+p['phi'])/p['rho']

        return {'R(S,B1)': rs1, 'R(S,B2)': rs2, 'R(B1,B2)': r12, 'sqrt': sq, 'b2max': b2max}
