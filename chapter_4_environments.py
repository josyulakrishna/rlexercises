BLOCKED = 1
TERMINAL = 16

class grid_environment: 
# actions=[up down left right ]
    def __init__(self):  
        self.states = range(15)
        self.actions = range(4)
#returns +1 for all possible transitions and 0 for rest 
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


#Returns -1 reward for all possible transitions, i.e up, down, left, right
#stay in the same block(only for boundary boxes or cells near an obstacle)
#except the goal which has reward of 0
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

    def get_next_state(self, s, a):
        # actions=[up,0 down,1 left,2 right,3 ]
            pos_s = None
            if a==0 and s>1 and s<5:
                pos_s=s
            elif a==3 and s%8==0:
                pos_s=s
            elif a==2 and s%8==1:
                pos_s=s
            elif a==1 and s>12 and s<15
                pos_s=s
            else:
                #pos_s=[(bump):s, 0:up:s-4, 1:down:s+4, 2:left:s-1, 3:right:s+1]
                if a==0:
                    pos_s = s-4
                if a==1: 
                    pos_s = s+4
                if a==2:
                    pos_s = s-1
                if a==3:
                    pos_s = s+1
            return pos_s