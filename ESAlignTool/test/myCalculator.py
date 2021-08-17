#!/usr/bin/env python

variables = [ "ESpFdX","ESpFdY","ESpFdZ","ESpFdAlpha","ESpFdBeta","ESpFdGamma","ESpRdX","ESpRdY","ESpRdZ","ESpRdAlpha","ESpRdBeta","ESpRdGamma","ESmFdX","ESmFdY","ESmFdZ","ESmFdAlpha","ESmFdBeta","ESmFdGamma","ESmRdX","ESmRdY","ESmRdZ","ESmRdAlpha","ESmRdBeta","ESmRdGamma" ]

def init(): #{{{
    d = {}
    for v in variables:
        d[v] = 0
    return d
#}}}
def accumulate_corrections():
    d = init()
    myfile = "inputMatrixElements_cfi.py"

    # read values
    fin = open(myfile, 'r')
    for line in fin.readlines():
        if '#' in line or not 'Iter' in line:
            continue
        for v in variables:
            if v in line:
                value = float( line.strip().split('(')[1].split(')')[0] )
                d[v] += value
                #if v == 'ESpFdX':
                #    print v, value
    fin.close()

    # print result
    for v in variables:
        print v, d[v]

if __name__ == "__main__":
    accumulate_corrections()
