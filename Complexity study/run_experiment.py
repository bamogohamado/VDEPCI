#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb  3 17:46:49 2026

@author: M. BAMOGO HAMADO
         Étudiant en Recherche Opérationnelle
"""

import matplotlib.pyplot as plt
import seaborn as sns
from experiment_data import run_experiment

# ------------------------------
# Run the Experiment
# ------------------------------

voter_sizes = [100, 500, 1000, 2000, 4000, 10000]
candidate_sizes = [3, 5, 7, 10, 15, 20]
df_results = run_experiment(voter_sizes, candidate_sizes)

# ------------------------------
# Analysis and High-Quality Visualization
# ------------------------------

time_stats = df_results.groupby(["n_voters", "n_candidates"])["time_sec"].mean().reset_index()

# Set seaborn style
sns.set(style="whitegrid", palette="muted", font_scale=1.2)

plt.figure(figsize=(16, 9), dpi=300)  # Large size & High resolution
palette = sns.color_palette("rocket", len(candidate_sizes))

sns.lineplot(
    data=time_stats,
    x="n_voters",
    y="time_sec",
    hue="n_candidates",
    palette=palette,
    marker='o'
)

plt.title("Average Execution Time of VDEPCI", fontsize=16)
plt.xlabel("Number of voters", fontsize=14)
plt.ylabel("Time (s)", fontsize=14)
plt.legend(title="Number of candidates", fontsize=12, title_fontsize=13)
plt.grid(True, linestyle='--', alpha=0.6)
plt.tight_layout()

# Save as high-resolution PNG
plt.savefig("VDEPCI_Execution_Time.png", dpi=600, bbox_inches='tight')

plt.show()



