





class Parameters():

    def __init__(self, inits_names, params, globals, inits):
        self.params = params
        self.globals = globals
        self.inits = inits
        self.inits_names = inits_names

    def get_params(self):
        return self.params

    def get_globals(self):
        return self.globals

    def get_inits(self):
        return self.inits

    def get_inits_names(self):
        return self.inits_names