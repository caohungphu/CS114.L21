nam_str = ["lios", "etr", "initis"]
nu_str = ["liala", "etra", "inites"]

def GetGioiTinh(word):
    for str in nam_str:
        if (str == word[-len(str):]):
            return 1
    for str in nu_str:
        if (str == word[-len(str):]):
            return 0
    return -1

def GetLoaiTu(word):
    for i in range(len(nam_str)):
        if (word[-len(nam_str[i]):] == nam_str[i]):
            return i
    for i in range(len(nu_str)):       
        if (word[-len(nu_str[i]):] == nu_str[i]):
            return i
    return -1

def CheckDanhTu(loaitu):
    if loaitu.count(1) != 1 and len(loaitu) > 1:
        return False
    return True

def CheckNguPhap(loaitu):
    for i in range(len(loaitu) - 1):
        if (loaitu[i] > loaitu[i+1]):
            return False
    return True

def CheckCungGioiTinh(gioitinh):
    for gioi in gioitinh:
        if (gioi != gioitinh[0]):
            return False
    return True

words = list(input().split())
gioitinh = [GetGioiTinh(word) for word in words]
loaitu = [GetLoaiTu(word) for word in words]

result = True

if (gioitinh.count(-1) != 0 or loaitu.count(-1) != 0):
    result = False
if (CheckDanhTu(loaitu) == False):
    result = False
if (CheckNguPhap(loaitu) == False):
    result = False
if (CheckCungGioiTinh(gioitinh) == False):
    result = False

if result:
    print("YES")
else:
    print("NO")