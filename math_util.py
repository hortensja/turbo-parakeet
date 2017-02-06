from __future__ import division
import numpy.random as nprand

def normalize_initial_conditions(conds):
    s = sum(conds)
    if s <= 0:
        return [0.25 for c in conds]
    ret = [round(c/s, 3) for c in conds]
    ret[-1] = 1-sum(ret[0:3])
    print(ret)
    return ret

def randomize_initial_conditions(length = 4, span = (0, 10)):
    conds = nprand.randint(span[0], span[1], length)
    print(conds)
    return normalize_initial_conditions(conds)

def round_params(p_dict, prec=5):
    ret = {}
    for n, p in p_dict.iteritems():
        try:
            ret[n] = round(p, prec)
        except TypeError:
            ret[n] = p
    return ret
