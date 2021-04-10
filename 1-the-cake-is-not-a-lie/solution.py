def leftRotateString(s, d):
    tmp = s[d : ] + s[0 : d]
    return tmp
    
def isLeftover(slice, s):
    return s != leftRotateString(s, len(slice))

def MaxNumbEqualSliceWithoutLeftover(s):
    n = len(s)
    d = dict() #k:slice type v:number of equal slices
    
    #generate all type of slices and its respective number of
    #equal slices
    for i in range(n):
        sliceType = ""
        for j in range(i, n):
            sliceType += s[j]
            if(sliceType in d.keys()):
                d[sliceType] += 1
            else:
                d[sliceType] = 1
    
    #Obtains the maximum number of equal slices without leftover
    maxNumbEqualSlices = 0
    sliceTypeMax = ""
    for sliceType in d:
        if ((not isLeftover(sliceType, s)) 
            and (d[sliceType] >= maxNumbEqualSlices)): 
                maxNumbEqualSlices = d[sliceType] 
                sliceTypeMax = sliceType
                
    return maxNumbEqualSlices