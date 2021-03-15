hs = int(input())
de = int(input())
p = int(input())
q = int(input())
vitriBobtruoc = 0
vitriBobsau = 0
vitriBob=0
x =0
y =0
vitriAlice = (p-1)*2 + q
vitriBobsau = vitriAlice + de
vitriBobtruoc = vitriAlice - de
if(vitriBobtruoc > 0):
    vitriBob = vitriBobtruoc
elif(vitriBobsau <= hs):
    vitriBob = vitriBobsau
else:
    vitriBob = -1
if vitriBob%2 ==0:
    y = 2
    x = vitriBob/2
else:
    y = 1
    x = round(vitriBob/2 +0.5)
if(vitriBob==-1):
    print(-1)
else:
    print(int(x),y)