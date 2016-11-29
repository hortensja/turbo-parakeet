from __future__ import division

def normalize_initial_conditions(conds):
    s = sum(conds)
    #print('sum: ', s)
    return [c/s for c in conds]