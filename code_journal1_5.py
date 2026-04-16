#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr 14 23:11:37 2026

@author: momokakume
"""

import numpy as np
from astropy.table import Table
from astropy.io import ascii
    
def table(x,y):
    data = Table([x,y], names = ['x', 'sin(x)'])
    ascii.write(data, 'table.txt', format='commented_header', overwrite=True)
    data_in = ascii.read('table.txt')
    return data_in

def main():
    x = np.linspace(0, 2*np.pi, 1000)
    y = np.sin(x)
    
    print (table(x,y))
    
if __name__ == '__main__':
    main()