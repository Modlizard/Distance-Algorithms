#Levenshtein distance function
#Compares two strings returns Levenshtein distance as integer
#03/07/2021 Modlizard
def lev(a,b):
    if type(a) != str or type(b) != str:
        raise Exception('Non-string arguments provided!')
    elif a == b:
        return 0
    elif len(a) == 0:
        return len(b)
    elif len(b) == 0:
        return len(a)
    elif a[0] == b[0]:
        return lev(a[1:],b[1:]) #[1:] means all characters but the first
    else:
        result = 1 + min(lev(a[1:],b),     #Deletion
                         lev(a,b[1:]),     #Insertion
                         lev(a[1:],b[1:])) #Replacement
        return result
