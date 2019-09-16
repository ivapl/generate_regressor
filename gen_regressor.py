import numpy as np
import math
from matplotlib import pyplot as plt
from sklearn import linear_model


def gen_stim_onset(length, tpoints, tau):
    # units in frames
    stim = np.zeros(length)
    stim[tpoints] = 1
    exp = []

    kernel = np.ones(tau)

    # Generate exponential function
    for counter, val in enumerate(kernel):
        exp.append(((1 / float(tau)) * math.exp((-counter / float(tau))))*val)
    #print len(exp)

    # Convolve the step function with exponential function
    onset = np.convolve(stim,exp)
    onset2 = [float(i) for i in onset]
    onset2 = onset2[0:-tau+1]
    #print len(onset2)

    return onset2
