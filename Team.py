class Team:
    pct1 = 0
    pct2 = 0
    pct3 = 0
    turnover_rate = 0
    oboard_rate = 0
    foul_rate = 0

    def __init__(self, ft, pct3, pct2):
        self.ft = ft
        self.pct3 = pct3
        self.pct2 = pct2