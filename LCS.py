#Longest Common Subsequence function
#Compares two strings returns Longest Common Subsequence as an integer
#03/07/2021 Modlizard
def lcs(a,b):
    if type(a) != str or type(b) != str:
        raise TypeError('Non-string comparison parameters provided!')
    else:
        calcArr = [[None]*(len(b)+1) for x in range(len(a)+1)]

        for x in range(len(a)+1):
            for y in range(len(b)+1):
                if y == 0 or x == 0:
                    calcArr[x][y] = 0
                elif a[x-1] == b[y-1]:
                    calcArr[x][y] = calcArr[x-1][y-1]+1
                else:
                    calcArr[x][y] = max(calcArr[x-1][y], calcArr[x][y-1])
        
        print(calcArr)
        return calcArr[x][y]

print(lcs('aabcdef','and abacus define'))