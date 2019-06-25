#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sat Jan 28 17:28:17 2017

@author: esther
"""


lambda x: np.trapz(plt.hist(x, Xbins, "histtype": "step"), x = Xbins)

rtCorrectInts = rt[correct].stack().groupby(level = ["Phase","Animal"]).apply(plt.hist,*args, **kwargsHist).apply(np.trapz, **{"x": Xbins})


rtCorrectInts = rt[correct].stack().groupby(level = ["Phase","Animal"]).apply(lambda i: np.trapz(lambda h: plt.hist(h, Xbins, "histtype": "step"), x = Xbins[:-1]))