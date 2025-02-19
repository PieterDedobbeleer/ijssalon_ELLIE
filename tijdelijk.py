from helper import decoreer

def print_aanbieding():
    prijzen = {
        "aardbei":3,
        "vanille":4,
        "chocolade":5
    }
    aanbieding = prijzen["aardbei"] * 0.8
    aanbieding_afgerond = round(aanbieding,2)
    reclame_tekst = "Vandaag in de aanbieding: vanille ijs, 1  liter slechts $"
    reclame_tekst_3 = reclame_tekst.upper()
    #reclame_tekst_4 = ["Vandaag","in","de","aanbieding:","vanille","ijs, ","1","liter","slechts","$", aanbieding_afgerond]
    reclame_tekst_4 = reclame_tekst_3.split()
    for el in reclame_tekst_4:
        #print(el.lower())
        if len(el) > 5:
            print(el.upper())
        else :
            print(el.lower())
    print(aanbieding_afgerond)

decoreer("aanbieding")

print_aanbieding()
    