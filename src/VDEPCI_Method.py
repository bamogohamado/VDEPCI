#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb  3 16:41:56 2026

@author: M. BAMOGO HAMADO
         Étudiant en Recherche Opérationnelle
"""

import numpy as np
import pandas as pd


# ==============================================================
#                       LES FONCTIONS                          #
#===============================================================

def LoadData(csv_file):
    df = pd.read_csv(csv_file, sep = ';')
    candidates = df.columns.tolist()
    vote_matrix = df.values
    return vote_matrix, candidates

def DistanceManhattan(vote_matrix):
    d1 = np.sum(np.abs(vote_matrix - 4), axis=0)
    return d1


def DistanceEuclidean(vote_matrix):
    d2 = np.sqrt(np.sum((vote_matrix - 4) ** 2, axis=0))
    return d2


def vdepci_method(csv_file):
    
    # Step 1: Load data
    X, candidates = LoadData(csv_file)

    # Step 2: Distance from Manhattan
    d1 = DistanceManhattan(X)
    d2 = DistanceEuclidean(X)
    min_d1 = np.min(d1)
    min_d1_indices = np.where(d1 == min_d1)[0]


    if len(min_d1_indices) == 1:
        winner = candidates[min_d1_indices[0]]
    else:
        # Step 3: Tie - compute d2
        d2_tied = d2[min_d1_indices]
        min_d2 = np.min(d2_tied)
        min_d2_indices = np.where(d2_tied == min_d2)[0]

        if len(min_d2_indices) == 1:
            winner = candidates[min_d1_indices[min_d2_indices[0]]]

    return candidates, d1, d2, min_d1_indices, winner
    