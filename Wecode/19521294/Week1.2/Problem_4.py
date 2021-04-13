def convert(latin):
    latin = latin.split()
    for i in range(len(latin)):
        if "liala" in latin[i][-6:]: latin[i] = 4
        elif "etra" in latin[i][-6:]: latin[i] = 5
        elif "inites" in latin[i][-6:]: latin[i] = 6
        elif "lios" in latin[i][-6:]: latin[i] = 1
        elif "etr" in latin[i][-6:]: latin[i] = 2
        elif "initis" in latin[i][-6:]: latin[i] = 3
        else: latin[i] = 7
    return latin
def check(latin):
    if 7 in latin:
        return False
    if len(latin)==1 and latin[0]==1:
        return True
    if (4 or 5 or 6) in latin:
        if (1 or 2 or 3) in latin:
            return False
        if latin.count(2) > 1: 
            return False
        danhtu = 0
        for i in range(len(latin)):
            if latin[i] == 5:
                danhtu = i
        for i in range(0,danhtu):
            if latin[i] == 6:
                return False
        for i in range(danhtu,len(latin)):
            if latin[i] == 4:
                return False
        return True       
    elif (1 or 2 or 3) in latin:
        if latin.count(2) > 1: 
            return False
        danhtu = 0
        for i in range(len(latin)):
            if latin[i] == 5:
                danhtu = i
        for i in range(0,danhtu):
            if latin[i] == 3:
                return False
        for i in range(danhtu,len(latin)):
            if latin[i] == 1:
                return False
        return True
    else: return True
latin = input()
latin = convert(latin)
if(check(latin)):
    print("YES")
else: print("NO")