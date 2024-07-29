def Possession(rate3, rate2, rate1, rate0):
    action = ""
    result = ""
    actions = ["attempt3", "attempt2", "turnover", "freethrows"]
    if action == "attempt3":
        #Find result
        if result == "make":
            return 3
        else:
            if result == "oboard":
                return Possession(rate3, rate2, rate1, rate0)
            else:
                return 0
    elif action == "attempt2":
        #Find result
        if result == "make":
            return 2
        else:
            if result == "oboard":
                return Possession(rate3, rate2, rate1, rate0)
            else:
                return 0
    elif action == "turnover":
        return 0
    elif action == "freethrows":
        #fix
        return 0