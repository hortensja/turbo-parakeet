from __future__ import division
from i_model import IModel


class Model(IModel):
    default_params = {'beta1': 0.4, 'beta2': 0.3, 'm1': 0, 'm2': 0, 'alpha': 0.05, 'gamma1': 0.05, 'gamma2': 0.2,
                      'mu': 0.05, 'nu': 0, 'xi': 0}

    def __init__(self, params=default_params):
        self.params = params

        # y = [s a b r]

    def get_set_of_ode(self, y, t):
        p = self.params

        def dsdt(y, t):
            return (
                p['mu'] - (p['mu'] + p['xi'] + p['m1'] + p['m2']) * y[0] - (p['beta1'] * y[1] + p['beta2'] * y[2]) * y[0] +
                p['nu'] * y[3])

        def dadt(y, t):
            return (p['m1'] * y[0] + p['beta1'] * y[1] * y[0] - (p['mu'] + p['alpha'] + p['gamma1']) * y[1])

        def dbdt(y, t):
            return (p['m2'] * y[0] + p['beta2'] * y[2] * y[0] - (p['mu'] + p['gamma2']) * y[2])

        def drdt(y, t):
            return (p['xi'] * y[0] + p['gamma1'] * y[1] + p['gamma2'] * y[2] - (p['mu'] + p['nu']) * y[3])

        return [dsdt(y, t), dadt(y, t), dbdt(y, t), drdt(y, t)]

    def get_legend(self):
        return ["S0", "A0", "B0", "R0"]

    def get_title(self):
        return 'SABR'

    def get_Rs(self):
        p = self.params

        r1 = (p['beta1']) / (p['mu'] + p['alpha'] + p['gamma1'])
        r2 = (p['beta2']) / (p['mu'] + p['gamma2'])

        lambda_ = p['mu'] + p['nu']
        theta = p['xi'] / (lambda_ + p['xi'])

        E0 = self.prepare_output((0, 0, theta))

        if p['m1'] > 0 or p['m2'] > 0:
            E0 = '-'
            E1 = '-'
            E2 = '-'
        else:
            lambda1 = p['beta1'] - p['mu'] - p['alpha'] - p['gamma1']
            lambda2 = p['beta2'] - p['mu'] - p['gamma2']
            kappa2 = lambda2 / (p['beta2'] * (lambda_ + p['gamma2']))
            rho1 = lambda1*p['beta2']/p['beta1']-lambda2
            rho2 = lambda1/p['beta1']
            rho2 /= (rho1*(lambda_+p['gamma1'])+p['alpha']*(lambda_+p['gamma2']))
            E1 = self.prepare_output((0, lambda_*kappa2, p['gamma2']*kappa2))
            abr = lambda_*rho1*rho2, p['alpha']*lambda_*rho2, p['gamma1']*rho1*rho2 + p['alpha']*p['gamma2']*rho2
            E2 = self.prepare_output(abr)

        return {'R1': r1 * (1 - theta), 'R2': r2 * (1 - theta), 'E0': E0, 'E1': E1, 'E2': E2}
