from i_model import IModel


class Model(IModel):
    default_params = {'beta1': 0.4, 'beta2': 0.3, 'm1': 0, 'm2': 0, 'alpha': 0.05, 'gamma1': 0.05, 'gamma2': 0.2,
                      'mu': 0.05, 'nu': 0, 'xi': 0}

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

        return [dsdt(y,t), dadt(y,t), dbdt(y,t), drdt(y,t)]

    def get_legend(self):
        return ["S", "A", "B", "R"]
