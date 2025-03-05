def mijn_functie_1(a):
    a == [2,4,10,12] 
    uitvoer = a**2
    print(uitvoer)
    #return uitvoer
#print(mijn_functie_1(12))

def mijn_functie_2a(a,b):
    uitvoer = [a+b,a-b,a*b,a/b]
    print(uitvoer)
    #return uitvoer
#print(mijn_functie_2a(13,3))

# het kan ook op deze manier

def mijn_functie_2b(a,b):
    uitvoer = []
    uitvoer.append(a+b)
    uitvoer.append(a-b)
    uitvoer.append(a*b)
    uitvoer.append(a/b)
    print(uitvoer)
    #return uitvoer
#print(mijn_functie_2b(100,20))

