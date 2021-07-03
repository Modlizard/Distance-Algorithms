#Hamming distance function
#Compares two strings returns Longest Hamming distance as an integer
#04/07/2021 Modlizard
def ham(a,b):
    if type(a) != str or type(b) != str:
        raise TypeError('Non-string comparison parameters provided!')
    elif len(a) != len(b):
        raise ValueError('Both parameters must be of the same length.')
    else:
        dist = 0
        for x in range(len(a)):
            if a[x] == b[x]:
                dist += 1
            else:
                pass
    
    return dist

#Alternatively this can be achieved in a one line statement:
# sum(xVal != yVal for xVal, yVal in zip(x,y))
#The zip function combines two equal length arrays in comma seperated pairs