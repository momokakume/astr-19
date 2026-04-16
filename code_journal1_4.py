#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr 14 14:56:18 2026

@author: momokakume
"""

class favorite_animal:
    def __init__ (self, arm_length, leg_length, eye_number, tail, furry):
        self.arm_length = float(arm_length)
        self.leg_length = float(leg_length)
        self. eye_number = int(eye_number)
        self.tail = bool(tail)
        self.furry = bool(furry)
        
    def print(self):
        print(f'My favorite animal has an arm length of {self.arm_length}cm.')
        print(f'It has a leg length of {self.leg_length}cm.')
        print(f'It has {self.eye_number} eyes.')
        if self.tail:
            print('It has a tail.')
        else:
            print('It does not have a tail.')
        if self.furry:
            print('It is furry.')
        else:
            print('It is not furry')
        
hedgehog = favorite_animal(10, 10, 2.0, True, False)

hedgehog.print()