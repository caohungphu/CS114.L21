ttnam = "lios "
ttnu = "liala "
dtnam = "etr "
dtnu = "etra "
dgtnam = "initis "
dgtnu = "inites "
list_nam=["lios ","etra ","initis "]
list_nu= ["liala ","etr ","inites "]
def check_nam(s):
    x1 = s.find(ttnu)
    x2 = s.find(dtnu)
    x3 = s.find(dgtnu)
    if(x1 != -1 or x2!=-1 or x3!=-1):
        return False
    else:
        s = s.replace('etr ','')
        s = s.replace('lios ','')
        s = s.replace('initis ','')
        if ' ' in s:
            return False
        else:
            return True
def check_nu(s):
    x1 = s.find(ttnam)
    x2 = s.find(dtnam)
    x3 = s.find(dgtnam)
    if(x1 != -1 or x2!=-1 or x3!=-1):
        return False
    else:
        s = s.replace('etra ','')
        s = s.replace('liala ','')
        s = s.replace('inites ','')
        if ' ' in s:
            return False
        else:
            return True
def check_danhtu(s,dt):
    y = s.find(dt)
    y1 = s.rfind(dt)
    if y==-1:
        return False
    elif y==y1:
        return True
    else:
        return False
def check_vitri(s,tt,dt,dgt):
    x = s.rfind(tt)
    y = s.find(dt)
    z = s.find(dgt)
    if (y > x and z!=-1 and y <z) or (z == -1 and y >x) :
        return True
    else:
        return False
def check_cau_nam(s):
    if check_nam(s) == True:
        if check_danhtu(s, dtnam) == True:
            if check_vitri(s, ttnam, dtnam, dgtnam) == True:
                return True
    else:
        return False
def check_cau_nu(s):
    if check_nu(s) == True:
        if check_danhtu(s, dtnu) == True:
            if check_vitri(s, ttnu, dtnu, dgtnu) == True:
                return True
    else:
        return False        
str_ = str(input())
str_ += " "
if check_cau_nam(str_) == True:
    print("YES")
else:
    if check_cau_nu(str_) == True:
        print("YES")
    else:
        print("NO")