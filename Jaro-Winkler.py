#Jaro-Winkler distance function
#Compares two strings returns Jaro-Winkler similarity as a float
#03/07/2021 Modlizard
def jaro(a,b):
    if type(a) != str or type(b) != str:
        raise TypeError('Non-string comparison parameters provided.')
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

def JaroWink(a,b,preLength,scaling=0.1,override=False): #In Winkler's work 0.1 is used as the standard scaling constant, soft prefix limit = 4
    if type(scaling) != float: #Raise errors for types and hard boundaries
        raise TypeError('Non-float scaling parameter provided.')
    elif type(preLength) != int:
        raise TypeError('Non-integer prefix length parameter provided.')
    elif type(override) != bool and override != 1 and override != 0:
        raise TypeError('Override must be a boolean datatype or boolean integer (0 or 1).')
    elif preLength < 0:
        raise ValueError('Prefix length parameter cannot be negative.')
    elif scaling < 0:
        raise ValueError('Scaling parameter cannot be negative')
    else:
        pass

    if not(override): #Raise errors for soft boundaries
        exception = ''
        
        if preLength > 4: exception += 'prefix length parameter greater than 4, '
        else: pass
        if preLength * scaling > 1.0: exception += 'prefix length * scaling multiplier greater than 1 - similarity potentially exceeds 1.0, '
        else: pass
        if exception == '': pass
        else: exception += 'specify parameter override=True to bypass these limits.'
        
        raise ValueError(exception.capitalize())
    else: 
        pass

    jaroSim = jaro(a,b)
    return jaroSim + preLength * scaling * (1 - jaroSim)
