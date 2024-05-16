# -*- coding: utf-8 -*-
"""
Created on Fri Oct 20 08:20:43 2023

@author: ADMIN
"""
#%% How to round properly

def round_half_up(iter_, dec_places=0):
    import fractions, math
    tmp=[]
    for i in iter_:
        sign = math.copysign(1,i)
        number_exact = abs(fractions.Fraction(i))
        shifted = number_exact * 10**dec_places
        shifted_trunc = int(shifted)
        if shifted - shifted_trunc >= fractions.Fraction(1, 2):
            result = (shifted_trunc + 1) / 10**dec_places
        else:
            result = shifted_trunc / 10**dec_places
        k = sign * float(result)
        tmp.append(k)
    return tmp
    

