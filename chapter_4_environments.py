BLOCKED = 1
TERMINAL = 16

class grid_environment: 
# actions=[up down left right ]
    def __init__(self):  
        self.states = range(15)
        self.actions = range(4)

    def tranisiton_probabilities(self, s, r, a, s_):
        pos_s=[s, s-4, s+4, s-1, s+1]
        if s_ in pos_s:
            if  pos_s.index(s_)-1==a and s_ >0: 
                if s_<16: 
                    if r == -1:
                        return 1.0
                    else: 
                        return 0
                elif s_ == 16 and r == 0: 
                    return 1
                
                elif s_ == 1 and r == -1: 
                    return 0 
                else: 
                    return 0
        else: 
            return 0

    def reward(self, s, a, s_):
        print s_, a, s
        pos_s=[s, s-4, s+4, s-1, s+1]
        if pos_s.index(s_)-1==a and s_>0 and s!=1:
            return -1
        if pos_s.index(s_)-1==a and s_>0 and s_==16:
            return 0
        if pos_s.index(s_)-1==a and s_>0 and s_>0 and s_==1:
            return -1
        else:
            return 0
