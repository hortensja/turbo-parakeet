from abc import ABCMeta, abstractmethod

class IModel:
    __metaclass__ = ABCMeta


    def set_params(self, new_params):
        self.params = new_params


    def update_param(self, param_name, param):
        try:
            self.params[param_name]
            self.params[param_name] = param
        except KeyError:
            print("Parameter doesn't exist")

    @abstractmethod
    def get_set_of_ode(self, y, t):
        pass

    @abstractmethod
    def get_legend(self):
        pass
