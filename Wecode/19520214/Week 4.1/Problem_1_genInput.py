import string, random
from textwrap import wrap


def genString(n):
    fullChars = string.ascii_uppercase + "               "
    count = 0
    result = ''
    while count < n:
        char = random.choice(fullChars)
        if (count == 0 or count == n - 1) and char == ' ':
            while char == ' ':
                char = random.choice(fullChars)
        result += char
        count += 1
    return result

def getResult_1(_str, n):
    result = wrap(_str, n, break_long_words = False)
    for i in result:
        i += ' '
    return result

def getResult_2(_str, n):
    result = []
    while len(_str) != 0:
        if len(_str) <= n:
            result.append(_str)
            return result
        if _str.find(' ') == -1:
            result.append(_str)
            return result
        else:
            if _str[n] != ' ':
                tmp = _str[:n]
                pos_space = tmp.rfind(' ')
                if pos_space != -1:
                    result.append(tmp[:pos_space + 1])
                    _str = tmp[pos_space + 1:] + _str[n:]
                else:
                    tmp = _str
                    pos_space = tmp.find(' ')
                    if pos_space != -1:
                        result.append(tmp[:pos_space + 1])
                        _str = tmp[pos_space + 1:]
                    else:
                        _str = tmp
            else:
                result.append(_str[:n])
                _str = _str[n:]
    return result

def getResult_3(_str, n):


def genTest(t, n):
    _ = 0
    while _ < t:
        print("======TEST:",_,"======")
        _str = genString(n)
        k = random.randrange(1, n)
        print("STRING:", _str)
        print("N:", k)
        print("Result 1:")
        print(getResult_1(_str, k))
        print("Result 2:")
        print(getResult_2(_str, k))
        print("======================")
        _ += 1


genTest(5, 10)