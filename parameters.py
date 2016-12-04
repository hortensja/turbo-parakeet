import random


class Parameters():

    def __init__(self, inits_names, params, globals, inits):
        self.params = params
        self.globals = globals
        self.inits = inits
        self.inits_names = inits_names
        self.all_dict = self.concatenate()

    def get_params(self):
        return self.params

    def get_globals(self):
        return self.globals

    def get_inits(self):
        return self.inits

    def get_inits_names(self):
        return self.inits_names

    def concatenate(self):
        inits = {}
        for i in range(len(inits)):
            inits[self.inits_names[i]] = inits[i]
        dict_p_g = dict(self.params, **self.globals)
        dict_p_g.update(inits)
        print('DICT_P_G:')
        print(dict_p_g)
        return dict_p_g

    def deconcatenate(self):
        for p in self.get_params():
            self.params[p] = self.all_dict[p]
        for g in self.get_globals():
            self.globals[g] = self.all_dict[g]
        for i_n in self.get_inits_names():
            ind = self.inits_names.index(i_n)
            self.inits[ind] = self.all_dict[i_n]

    def update(self):
        self.deconcatenate()
        self.all_dict = self.concatenate()

    def update_one(self, name, param):
        self.all_dict[name] = param

    def __str__(self):
        ret = []
        for i in range(len(self.get_inits_names())):
            ret.append(str(self.inits_names[i]+': '+str(self.inits[i])))
        return str(ret)#str([str(p+' '+str(self.params[p])) for p in self.params])#, str(self.globals), str(self.inits)

    @staticmethod
    def randomize_params(p_dict, p_min=0.0, p_max=1.0):
        ret = {}
        for name, p in p_dict.iteritems():
            ret[name] = random.uniform(p_min, p_max)
        print(ret)
        return ret
