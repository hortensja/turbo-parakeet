from __future__ import division
import numpy.random as nprand

def normalize_initial_conditions(conds):
    s = sum(conds)
    #print('sum: ', s)
    return [c/s for c in conds]

def randomize_initial_conditions(length = 4, span = (0, 10)):
    conds = nprand.randint(span[0], span[1], length)
    print(conds)
    return normalize_initial_conditions(conds)