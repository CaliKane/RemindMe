# -*- coding: utf-8 -*-
"""
Created on Thu Oct 29 23:34:53 2015

@author: steven
"""
import datetime
import matplotlib.pyplot as plt

#axes = Figure().add_subplot(111)
fig, axes = plt.subplots(figsize = (6, 1))

x = [1,2,3] #These are just for testing purposes


plt.scatter(x,[1]*len(x), color = 'c', s = 100, marker = 's')
plt.xlabel('Date')
plt.title('Event Timeline')

axes.yaxis.set_visible(False)
axes.spines['right'].set_visible(False)
axes.spines['left'].set_visible(False)
#axes.spines['top'].set_visible(False)
#axes.xaxis.set_ticks_position('bottom')


plt.show()
