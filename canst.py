def wordcanonicalStructure(string):
    def enumerateUnique(string):
        l1 = []                     
        listvariable = list(string)
        lengthvariable = len(list(string))-1
        pointer = 1
        for free in range(0,lengthvariable+1):
            if listvariable[free] != " ":
              if listvariable[free] not in l1:
                l1.append(listvariable[free])
        return(l1)
    v = enumerateUnique(string)
    tlots = list(string)
    lengthvariable = len(list(string))-1
    l = list()
    for thepointer in range(0,len(tlots)):
        if tlots[thepointer] != " ":
          l = list(l) + list(str(1+v.index(tlots[thepointer])))
        else: 
          l = list(l) + list(" ")
    print(str(l))
    