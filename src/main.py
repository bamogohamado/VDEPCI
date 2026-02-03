#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb  3 16:44:52 2026

@author: M. BAMOGO HAMADO
         Étudiant en Recherche Opérationnelle
"""

from VDEPCI_Method1 import vdepci_method

# Main program
csv_file = '/Users/macbookpro/Desktop/VDEPCI/Example4.csv'
cand, d1, d2, d1_min, winner = vdepci_method(csv_file)


# Output
print("d1_distances:", dict(zip(cand, d1)))
if len(d1_min) > 1:
    d2_tied = d2[d1_min]
    dd = {cand[d1_min[i]]: d2[i] for i in range(len(d2))}
    print("d2 distances (ties):", dd)
print(" The winning candidate is:", winner)

