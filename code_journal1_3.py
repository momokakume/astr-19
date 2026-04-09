#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr  8 16:37:31 2026

@author: momokakume
"""

def f(x):
    return x**3 + 8
    
def main():
    x = 9
    print (f(x))
  
    if f(x)>27:
        print('YAY!')
        
if __name__ == "__main__":
    main()