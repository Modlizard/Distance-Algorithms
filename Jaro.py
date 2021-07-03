#Jaro distance function
#Compares two strings returns Jaro similarity as a float
#03/07/2021 Modlizard
def jaro(a,b):
    if type(a) != str or type(b) != str:
        raise Exception('Non-string arguments provided!')
    elif a == b: 
        return 1.0
    else:
        #Match counting 
        mChars = 0 #Matching chars
        mDist = int(max(len(a),len(b))/2 - 1) #Max distance for matching chars
        
        connA = [False] * len(a) #If given character already has a connected match
        connB = [False] * len(b)

        for x in range(len(a)):
            for y in range(max(0, x-mDist), min(len(b), x+mDist + 1)): #Only compare characters based on mDist range
                if a[x] == b[y] and connB[y] == 0: #Every character of a will be checked once only so we check for pairing presence in b
                    connA[x], connB[y] = True, True
                    mChars += 1
                    break #This character in a has been paired so we break

        if mChars == 0:
            return 0.0

        #Transpositon counting
        t = 0 #Transpositions
        bPos = 0 #Current character being checked in b

        for x in range(len(a)):
            if connA[x]:
                while not(connB[bPos]): #Find next paired character in b
                    bPos += 1
                
                if a[x] != b[bPos]: #If the next paired character is different a transposition occurred
                    bPos += 1
                    t += 1

        t = t//2 #All but one or all transpositions were detected twice

        return (mChars/len(a) + mChars/len(b) + (mChars - t + 1) / mChars) / 3.0