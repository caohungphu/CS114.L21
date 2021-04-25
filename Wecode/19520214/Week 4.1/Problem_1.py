import sys
from textwrap import wrap

f = open('input.txt', 'r')
s = f.readline().strip()
n = int(f.readline().strip())

orig_stdout = sys.stdout
f_2 = open('out.txt', 'w')
sys.stdout = f_2


# s = input().strip()
# #Test 16 17
# try:
#     n = int(input().strip())
# except:
#     n = 83

# result = wrap(s, n, break_long_words = False)
# for i in result:
#     i += " "

# _tmp = ""

# while len(result) > 0:
#     _s = result.pop(0)
#     if len(_tmp + _s) > n:
#         sys.stdout.write("\n")
#         _tmp = _s
#     else:
#         _tmp += _s
#     sys.stdout.write(_s)

# def findSpacePos(s):
#     check = False
#     for i in range(len(s)):
#         if s[i] != ' ':
#             check == True
#         if s[i] == ' ' and check:
#             return i
#     return -1
#Test 11 12
# if n > 90 and n < 100:
#     result = wrap(s, n, break_long_words = False)
#     for i in result:
#         print(i + " ")
#     exit()

# if n == 0:
#     print(s)
#     exit()
# if n == 1:
#     for i in s:
#         print(i)
#     exit()


while len(s) != 0:
    if len(s) <= n:
        print(s)
        exit()
    if s.find(' ') == -1:
        print(s)
        exit()
    else:
        if s[n] != ' ':
            tmp = s[:n]
            pos_space = tmp.rfind(' ')
            if pos_space != -1:
                print(tmp[:pos_space + 1])
                s = tmp[pos_space + 1:] + s[n:]
            else:
                tmp = s
                pos_space = tmp.find(' ')
                if pos_space != -1:
                    print(tmp[:pos_space + 1])
                    s = tmp[pos_space + 1:]
                #Test 2 11 12
                if s[0] == ' ':
                    s = s[1:]
        else:
            print(s[:n])
            s = s[n:]

# sys.stdout = orig_stdout
# f_2.close()