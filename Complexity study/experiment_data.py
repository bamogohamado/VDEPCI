#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb  3 17:45:27 2026

@author: M. BAMOGO HAMADO
         Étudiant en Recherche Opérationnelle
"""


import numpy as np
import pandas as pd
import random
import time

# ------------------------------
# Generation and Methods
# ------------------------------

def generate_votes_matrix(n_voters, n_candidates, score_range=(0, 10)):
    return np.random.randint(score_range[0], score_range[1]+1, size=(n_voters, n_candidates))

def d1_fixed_base(X, base=4):
    return np.sum(np.abs(X - base), axis=0)

def d2_fixed_base(X, base=4):
    return np.sum((X - base)**2, axis=0)

def vdepci_method(X, candidates):
    d1 = d1_fixed_base(X)
    min_d1 = np.min(d1)
    indices_d1 = np.where(d1 == min_d1)[0]

    if len(indices_d1) == 1:
        return candidates[indices_d1[0]], 'd1'

    d2 = d2_fixed_base(X)
    d2_eq = d2[indices_d1]
    min_d2 = np.min(d2_eq)
    indices_d2 = np.where(d2_eq == min_d2)[0]

    if len(indices_d2) == 1:
        return candidates[indices_d1[indices_d2[0]]], 'd2'

    gagnant = random.choice(indices_d2)
    return candidates[indices_d1[gagnant]], 'tirage'

# ------------------------------
# Experiment Function
# ------------------------------

def run_experiment(voter_sizes, candidate_sizes, n_repeats=30):
    results = []
    for n_voters in voter_sizes:
        for n_candidates in candidate_sizes:
            for _ in range(n_repeats):
                X = generate_votes_matrix(n_voters, n_candidates)
                candidates = [f"C{i+1}" for i in range(n_candidates)]
                start = time.time()
                winner, method = vdepci_method(X, candidates)
                duration = time.time() - start
                results.append({
                    "n_voters": n_voters,
                    "n_candidates": n_candidates,
                    "winner": winner,
                    "method": method,
                    "time_sec": duration
                })
    return pd.DataFrame(results)
