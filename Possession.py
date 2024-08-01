import random as rand
import matplotlib.pyplot as plt

class Team:
    def __init__(self, ft_pct, two_pct, three_pct, to_rate, two_rate, three_rate, rebound_rate):
        self.ft_pct = ft_pct
        self.two_pct = two_pct
        self.three_pct = three_pct
        self.to_rate = to_rate
        self.two_rate = two_rate
        self.three_rate = three_rate
        self.rebound_rate = rebound_rate

# Shot function, return true if shot is a make, false if it misses
def Shot(pct):
    outcome = rand.uniform(0,100)
    return (outcome <= pct)

#Rebound: return true if a missed shot is rebounded by offense, false if not
def Rebound(pct):
    outcome = rand.uniform(0,100)
    return (outcome <= pct)

#Live FT: returns the outcomes of a live free throw
def LiveFT(team):
    if Shot(team.ft_pct):
        result = "FT Make"
        points = 1
        nextPoss = False
    else:
        points = 0
        if Rebound(team.rebound_rate):
            result = "FT Miss, offensive rebound"
            nextPoss = True
        else:
            result = "FT Miss, defensive rebound"
            nextPoss = False
    #print(result)
    return result, points, nextPoss

#Dead FT: returns the outcomes of a dead free throw (no rebounding opportunities, shooting team gets another FT)
def DeadFT(team):
    if Shot(team.ft_pct):
        result = "FT Make"
        points = 1
    else:
        result = "FT Miss"
        points = 0
    #print(result)
    return result, points, True

#FT: returns the outcomes of a free throw
def FT(team, type):
    if type == "live ft":
        return LiveFT(team)
    else:
        return DeadFT(team)

#Live Possession: returns the outcomes of a live possession
def LivePoss(team):
    outcome = rand.uniform(0,100)
    if outcome <= team.to_rate:
        result = "TO"
        points = 0
        nextPoss = False
    elif outcome <= (team.to_rate + team.two_rate):
        if Shot(team.two_rate):
            result = "2pt Make"
            points = 2
            nextPoss = False
        else:
            points = 0
            if Rebound(team.rebound_rate):
                result = "2pt Miss, offensive rebound"
                nextPoss = True
            else:
                result = "2pt Miss, defensive rebound"
                nextPoss = False
    else:
        if Shot(team.two_rate):
            result = "3pt Make"
            points = 3
            nextPoss = False
        else:
            points = 0
            if Rebound(team.rebound_rate):
                result = "3pt Miss, offensive rebound"
                nextPoss = True
            else:
                result = "3pt Miss, defensive rebound"
                nextPoss = False
    #print(result)
    return result, points, nextPoss

#Possession: returns possession outcomes (STRING description, INT points scored, BOOL possession maintained)
def Possession(team, type):
    if (team.to_rate + team.two_rate + team.three_rate != 100):
        print("team rates are invalid")
    if type == "live":
        return LivePoss(team)
    elif type == "live ft" or type == "dead ft":
        return FT(team, type)
    else:
        print("invalid possession type")
    
team = Team(ft_pct=80, two_pct=45, three_pct=35, to_rate=20, two_rate=50, three_rate=30, rebound_rate=15)
poss_result = Possession(team, "live ft")
print(poss_result)
scores = []
o_rebounds = []
d_rebounds = []
to_arr = []
for i in range(0,10000):
    score = 0
    rebounds_o = 0
    rebounds_d = 0
    to = 0
    for i in range(0,100):
        result, points, rebound = Possession(team, "live")
        score += points
        if result == "TO":
            to += 1
        if points == 0 and result != "TO":
            if (rebound):
                rebounds_o += 1
            else: rebounds_d += 1
    scores.append(score)
    o_rebounds.append(rebounds_o)
    d_rebounds.append(rebounds_d)
    to_arr.append(to)

for stat in [scores, o_rebounds, d_rebounds, to_arr]:
    plt.hist(stat)
    plt.show()
