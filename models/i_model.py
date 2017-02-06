from __future__ import division
from abc import ABCMeta, abstractmethod

class IModel:
    __metaclass__ = ABCMeta

    def set_params(self, new_params):
        for name, param in new_params.iteritems():
            print(name, param)
            self.update_param(name, param)

    def update_param(self, param_name, param):
        try:
            self.params[param_name]
            self.params[param_name] = param
        except KeyError:
            print("Parameter doesn't exist")

    def get_params(self):
        return self.params

    def prepare_output(self, x):
        ret = "("
        ret += str(round(1-sum(x), 3))
        for xx in x:
            if xx < 0:
                return '-'
            ret += ", "
            ret += str(round(xx, 3))
        ret += ")"
        return ret

    @abstractmethod
    def get_set_of_ode(self, y, t):
        pass

    @abstractmethod
    def get_legend(self):
        pass

    @abstractmethod
    def get_title(self):
        pass

    @abstractmethod
    def get_Rs(self):
        pass