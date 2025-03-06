from algemene_functies import mijn_functie_2a

#import algemene_functies
#algemene_functies.mijn_functie_2a(13,3)

def mijn_aanbieding_1(smaak,prijs,korting):
    prijs_na_korting = prijs * (1-korting)
    uitvoer = f"Vandaag in de aanbieding: emmertje ijs ( 1 liter ) in de smaak {smaak}, van {prijs} euro voor {prijs_na_korting} euro!!!"
    print(uitvoer)
mijn_aanbieding_1(f"aardbei",4,0.1)

#def inkomsten_totaal(inkomsten):
    #inkomsten+=[]
    #print(inkomsten)
#inkomsten_totaal([1+2+3+4+5+6+7])

def inkomsten_totaal(inkomsten,btw_procent):
    inkomsten+=[]
    inkomsten = float(inkomsten[0])
    btw = btw_procent/100
    btw_bedrag = inkomsten * btw
    print(f"Het totaal van alle inkomsten van deze week is {inkomsten} euro, waarover {round(btw_bedrag,2)} euro btw betaald dient te worden.") 
inkomsten_totaal([1+2+3+4+5+6+7], 20)

def laag_en_hoog(mijn_lijst):
    mijn_lijst==[]
    max_lijst = (max(mijn_lijst))
    min_lijst = (min(mijn_lijst))
    print(max_lijst,"= de max value","en",min_lijst,"is de min value")
laag_en_hoog([1,2,3,110,299,300,227])

def gemiddelde(mijn_lijst):
    totaal = 0
    for i in mijn_lijst:
        totaal+=i
    #mijn_lijst=int(mijn_lijst[0])
    gemiddelde = totaal/len(mijn_lijst)
    print(f"De gemiddelde inkomsten van deze week zijn {round(gemiddelde,2)} Euro!")
gemiddelde([20,234,212,453,387,987,43])

def meervoudig(invoer_lijst):
    mijn_lijst=[]
    mijn_lijst=invoer_lijst
    print(laag_en_hoog(mijn_lijst))
meervoudig([2,3,4,5,99,4242,0,7272])

def combinatie(invoer_lijst_2):
    korte_lijst=laag_en_hoog(invoer_lijst_2)
    uitvoer=mijn_functie_2a(korte_lijst[0],korte_lijst[1])
    return uitvoer
    


