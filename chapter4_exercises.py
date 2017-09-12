import numpy as np
from collections import defaultdict
import chapter_4_environments.grid_environment

#generic value iteration 
def iterative_policy_evalutation(policy, states, actions, theta, gamma): 
    V = defaultdict(float)
    v = defaultdict(float)
    ge = chapter_4_environments.grid_environment()
    delta = 0
    while(delta<theta): 
       for i in len(states): 
            v[states[i]] = V[states[i]]
            # Reward for action 
            # Possible actions actions=[0:up 1:down 2:left 3:right]
            # Here one action is chosen randomly on  a uniform distribution
            a = np.random.choice([0,1,2,3], 1)
            s_ = ge.get_next_state(s, a)
            r = ge.reward(i, a, s_)
            p_a_s = ge.tranisiton_probabilities(s, r, a, s_)
            V[states[i]] = p_a_s*(r+gamma*v[s_])
            delta  = max(delta, abs(v[s_]-V[s_]))
