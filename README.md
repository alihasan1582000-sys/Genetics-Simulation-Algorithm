# 🧬 Terminal Evolution: Genetic Algorithm Optimizer

A zero-dependency, real-time visualization of a Genetic Algorithm evolving random strings to reach a target sequence, rendered entirely in the terminal.

## 🚀 Overview

This project is a from-scratch Python implementation of a stochastic optimization technique inspired by Darwinian evolution. It demonstrates how complex solutions can emerge from random noise through the principles of selection, crossover, and mutation.

Instead of just printing logs, this script features a custom CLI dashboard with a live-updating ASCII learning curve, crossover tree, and population leaderboard.

## ✨ Features

* **Zero Dependencies:** Built entirely with Python standard libraries (`random`, `math`, `os`, `time`, `string`).
* **Live ASCII Dashboard:** Renders a frame-by-frame UI tracking the evolution process.
* **Fitness Tracking Graph:** A sliding area chart showing the best fitness score percentage across generations.
* **Object-Oriented Design:** Encapsulates biological concepts into programmatic structures (e.g., the `DNA` class).
* **Dynamic Mating Pool:** Uses fitness-weighted probability (a roulette-wheel selection algorithm) to determine the next generation.

## 🛠️ How It Works

The algorithm follows four main biological phases:

1. **Initialization:** Generates a population of 400 random strings (DNA sequences) using the allowed gene pool (letters and spaces).
2. **Fitness Evaluation:** Scores every string based on how many characters match the target string exactly.
3. **Selection & Crossover (Recombination):** The highest-scoring strings are placed into a mating pool. Two parents are randomly selected (with higher probability for fitter parents) and their strings are spliced together at a random midpoint to create a child.
4. **Mutation:** To prevent premature convergence and maintain genetic diversity, each character in a child's sequence has a 1% chance of mutating into a completely random character.

The cycle repeats until a child sequence achieves a 100% fitness score.
