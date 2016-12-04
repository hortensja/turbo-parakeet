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

    @abstractmethod
    def get_set_of_ode(self, y, t):
        pass

    @abstractmethod
    def get_legend(self):
        pass

    @abstractmethod
    def get_title(self):
        pass