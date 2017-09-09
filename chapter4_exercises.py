import numpy as np
from collections import defaultdict

def iterative_policy_evalutation(policy, states, actions): 
    V = defaultdict(float)
    v = defaultdict(float)
    while: 
       deltas = 0
       for i in len(states): 
           v[states[i]] = V[states[i]]
           V[states[i]] = [for a in actions]