from __future__ import division
import numpy.random as nprand

def normalize_initial_conditions(conds):
    s = sum(conds)
    return [round(c/s, 3) for c in conds]

def randomize_initial_conditions(length = 4, span = (0, 10)):
    conds = nprand.randint(span[0], span[1], length)
    print(conds)
    return normalize_initial_conditions(conds)

def round_params(p_dict, prec=5):
    ret = {}
    for n, p in p_dict.iteritems():
        ret[n] = round(p, prec)
    return ret
