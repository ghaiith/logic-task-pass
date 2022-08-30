def removeChar(str,char):
    newStr = str.translate({ord(char): None})
    str=newStr
    return str

def findPrimeNumber(n):
    for i in range(0, n + 1):
        if i > 1:
            for z in range(2, i):
                if (i % z) == 0:
                    break
            else:
                print(i)

def countChar(str,char):
    count =0
    for i in str:
        if i == char:
            count+=1
    return count


