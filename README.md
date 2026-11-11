<div align="center">

# AiLab

### Building neural networks from scratch, one experiment at a time.

**Project Frankenstein** — a hands-on exploration of neural networks, gradient descent, and backpropagation using Python.

![Python](https://img.shields.io/badge/Python-3776AB?style=flat-square&logo=python&logoColor=white)
![Status](https://img.shields.io/badge/status-work%20in%20progress-FFA500?style=flat-square)
![Focus](https://img.shields.io/badge/focus-neural%20networks-6C63FF?style=flat-square)

</div>

---

## Overview

**AiLab** is my personal machine learning playground. Rather than starting with a high-level ML framework, I'm implementing the fundamentals myself to understand what happens inside a neural network — from a single weighted input to a multilayer network trained with backpropagation.

The goal isn't to build the next large language model overnight. It's to understand the math, write the algorithms, break things, investigate why they broke, and gradually turn the experiments into a reusable neural-network engine.

> **Philosophy:** Understand the machinery before relying on the abstractions.

## What's implemented

- **Single-neuron training:** weighted inputs, bias, prediction error, and gradient-based updates.
- **Training on multiple samples:** learning a relationship rather than fitting only one input.
- **Learning curves:** tracking mean absolute error with Matplotlib.
- **Manual multilayer network:** two inputs, a two-neuron hidden layer, and one output.
- **Backpropagation:** manually computing gradients and updating weights and biases.
- **Activation functions:** ReLU, Leaky ReLU, identity, and their derivatives.
- **Generalization experiments:** comparing training performance with unseen inputs, including negative numbers.

The code is deliberately explicit and educational. These are **learning experiments**, not a production ML library.

## Repository structure

```text
AiLab/
├── ativacao.py       # Activation functions and derivatives
├── neuron.py         # First neuron and basic gradient descent
├── neuronV2.py       # Multiple training examples + loss visualization
├── rede.py           # First multilayer network experiment
├── redeLinear.py     # Multilayer network with identity activation
├── soma.py           # Early experiment / placeholder
└── README.md
```

Each script represents a step in the learning process, including early implementations that are retained for reference.

## The math behind it

A neuron starts with a weighted sum:

$$
z = \sum_{i=1}^{n} w_i x_i + b
$$

An activation function transforms it:

$$
a = f(z)
$$

During training, the network measures the difference between its prediction and the expected output, then updates its parameters using gradients. For the single-neuron experiments, the update follows the gradient of a half-squared-error objective:

$$
w_i \leftarrow w_i - \eta (\hat{y} - y)x_i
$$

where $\eta$ is the learning rate. The multilayer experiments extend this idea through the chain rule (backpropagation).

## An experiment: learning addition

The linear-network experiment trains on examples of two-number addition, including positive, negative, mixed-sign, and zero inputs.

The important lesson wasn't just getting a low training error: **the choice of activation function changes the behavior of the network**. ReLU-based experiments exposed difficulties with negative inputs, while an identity-activation network can represent addition directly because addition is linear.

This is also a reminder that good results on training samples do not automatically imply good generalization.

## Getting started

Clone the repository:

```bash
git clone https://github.com/raio2188/AiLab.git
cd AiLab
```

Run one of the standard-library experiments:

```bash
python neuron.py
python rede.py
python redeLinear.py
```

For the learning-curve experiment, install its plotting dependencies:

```bash
python -m pip install matplotlib PyQt6
python neuronV2.py
```

> `neuronV2.py` explicitly selects Matplotlib's `QtAgg` backend, so a compatible Qt binding is needed to display its plot.

## Roadmap

- [x] Implement a neuron from scratch
- [x] Implement manual gradient updates
- [x] Train on multiple examples
- [x] Plot training error
- [x] Build a small multilayer network
- [x] Explore activation functions and backpropagation
- [ ] Replace hard-coded weights with configurable layers
- [ ] Implement vectorized operations and matrix-based computation
- [ ] Add automated tests and reproducible benchmarks
- [ ] Train on more challenging, nonlinear datasets
- [ ] Experiment with reusable neural-network modules
- [ ] Explore orchestration of specialized models

These are goals, not completed features.

## Why build this?

Frameworks like PyTorch and TensorFlow are extremely useful, but I want to understand the mechanisms they abstract away. AiLab documents that process in code: small experiments, mistakes, corrections, and gradually more capable models.

The project is ongoing, and the implementation will evolve as I learn.

---

<div align="center">

**Made to learn, not to pretend the hard parts don't exist.**

[Repository](https://github.com/raio2188/AiLab)

</div>
