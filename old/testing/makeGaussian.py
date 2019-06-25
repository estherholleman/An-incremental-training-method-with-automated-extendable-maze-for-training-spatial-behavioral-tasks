#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Thu Jan 26 14:48:55 2017

@author: esther
"""

import numpy as np
import matplotlib.pyplot as plt


mu, sigma = 2000, 100 # mean and standard deviation
s = np.random.normal(mu, sigma, 5000)

#plt.hist(s, 30, normed=True)
Xbins = range(0,3000)
#count, bins, ignored = plt.hist(s, 30, normed=True)
count, bins, ignored = plt.hist(s, Xbins, normed=True)
plt.plot(bins, 1/(sigma * np.sqrt(2 * np.pi)) *
np.exp( - (bins - mu)**2 / (2 * sigma**2) ),
linewidth=2, color='r')
plt.show()

print np.trapz(s)

snorm = (s - min(s)) / (max(s) - min(s))

binsize = np.mean(np.diff(bins))

#print np.trapz(snorm,s)
print np.trapz(count,Xbins[:-1])
