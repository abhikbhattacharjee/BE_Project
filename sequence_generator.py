# -*- coding: utf-8 -*-
"""
Created on Wed Aug 28 11:59:25 2019

@author: Abhik

"""
import numpy as np

BASES = ('A', 'C', 'T', 'G')
P = (0.260, 0.240, 0.260, 0.240)

def random_dna_sequence(length):
    return ''.join(np.random.choice(BASES, p=P) for _ in range(length))

with open('dna.txt', 'w+') as txtout:
    for _ in range(10):
        dna = random_dna_sequence(602)
        txtout.write(dna)
        txtout.write("\n")

        print (dna)