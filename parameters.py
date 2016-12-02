





class Parameters():

    def __init__(self, params, globals, inits):
        self.params = params
        self.globals = globals
        self.inits = inits

    def get_params(self):
        return self.params

    def get_globals(self):
        return self.globals

    def get_inits(self):
        return self.inits