# Luodaan tietokanta Työkalujen lainaus-järjestelmälle



#



# Sanakirjat
unit_price={}
description={}
stock={}

# Avataan saldo-tiedosto
details = open("saldo.txt","r")

# Ensimmäinen luku on saldoilla oleva tavaramäärä
no_items  = int((details.readline()).rstrip("\n"))

# Lisää kohteita sanakirjoihin
for i in range(0,no_items):
    line  = (details.readline()).rstrip("\n")
    x1,x2 = line.split("#")
    x1=int(x1)
    x2=float(x2)
    unit_price.update({x1: x2})

for i in range(0,no_items):
    line  = (details.readline()).rstrip("\n")
    x1,x2 = line.split("#")
    x1=int(x1)
    description.update({x1: x2})

for i in range(0,no_items):
    line  = (details.readline()).rstrip("\n")
    x1,x2 = line.split("#")
    x1=int(x1)
    x2=int(x2)
    stock.update({x1: x2})

details.close()

# Lista ostettujen tuotteiden tallentamiseen
cart=[]

c="k" # Suorittaa while-loopin niin kauan kuin käyttäjä haluaa


# Ohjeet
print()
print("Ohjelman Toiminnot")
print("A - Lisää (inventoi) tuote saldoille")
print("R - Poista (inventoi) tuote saldoilta")
print("E - Muokkaa tuotteen tietoja")
print("L - Listaa kaikki tuotteet")
print("I - Näytä tuotteen tiedot")
print("P - Lainaa")
print("V - Vahvista lainaus")
print("S - Näytä kaikki lainattavat tuotteet")
print("Poista - Poista tuote lainaslistalta")
print("Valikko - Tämä valikko uudelleen") # Mahdollisesti tulee käyttövirheitä kirjoittaessa "valikko" tai "v" joilla on eri toiminnot
print("Tämä ohjelma on vielä kehitysvaiheessa ja tähän tulee vielä muutoksia.")
print()


total_cost=0 
flag=0 

while(c!= "q" or c!= "Q"):
    c= input("Valikko -> valikkoon , q -> lopeta ohjelma. Mitä haluat tehdä?   ")
    
    if(c=="q" or c=="Q"):
        break
        
    elif(c=="A" or c=="a"):# Lisää tuotteen saldoille
        p_no = int(input("Kirjoita tuotenumero: "))
        p_pr = float(input("Kirjoita tuotteen hinta: "))
        p_desc = input("Kirjoita tuotteen nimi: ")
        p_stock = int(input("Anna tuotteen lukumäärä: "))
        
        m=0
        for i in range(0,len(unit_price)):
            if(p_no in unit_price):
                p_no+=1
                m=1
        if(m==1):
            print()
            print("Tuotenumero on jo olemassa :(, muutetaan arvo ",p_no)
                
        unit_price.update({p_no: p_pr})
        description.update({p_no: p_desc})
        if(p_stock > -1):
            stock.update({p_no: p_stock})
        else:
            p_stock = 0
            stock.update({p_no: p_stock})
            print("Luku ei voi olla negatiivinen, Saldo nollattu.")
        print()
        print("Tuotenumero: ",p_no," Kuvaus: ",description.get(p_no)," Hinta: ",unit_price.get(p_no)," Varastosaldo: ",stock.get(p_no))
        print("Tuote lisätty onnistuneesti!")
        print()
        
    elif(c=="E" or c=="e"):# Muokkaa tuotteita
        print()
        p_no = int(input("Kirjoita osanumero: "))
        if(p_no in unit_price):
            p_pr = float(input("Syötä tuotteen hinta: "))
            p_desc = input("Kirjoita tuotteen nimi: ")
            p_stock = int(input("Kirjoita osanumero: "))
                
            unit_price.update({p_no: p_pr})
            description.update({p_no: p_desc})
            stock.update({p_no: p_stock})
            
        else:
            print("Tuotetta ei ole valikoimassa, lisätäksesi tuotteen valikoimaan paina a")
        print()
    
            
    elif(c=="R" or c=="r"):# Poistaa (inventoi) tuotteen saldoilta
        p_no = int(input("Kirjoita osanumero: "))
        if(p_no in unit_price):
            are_you_sure = input("Haluatko varmasti poistaa tuotteen (k/e)? ")
            if(are_you_sure=="k" or are_you_sure=="K"):
                unit_price.pop(p_no)
                description.pop(p_no)
                stock.pop(p_no)
                print("Tuote poistettu onnistuneesti!")
            print()
        else:
            print("Pahoittelut, Tuotetta ei ole valikoimassamme!")
            print()
        
    elif(c=="L" or c=="l"):# Listaa kaikki tuotteet
        print()
        print("Tuotenumerot ja niiden hinnat: ",unit_price)
        print("Tuote: ",description)
        print("Tuotteita varastossa: ",stock)
        print()

    elif(c=="I" or c=="i"):# Kysy tuotetiedot
        print()
        p_no=int(input("Syötä tuotenumero: "))
        if(p_no in unit_price):
            print()
            print("Tuotenumero: ",p_no," Kuvaus: ",description.get(p_no)," Hinta: ",unit_price.get(p_no)," Varastosaldo: ",stock.get(p_no))
            if(stock.get(p_no)<3 and stock.get(p_no)!=0):
                print("Vain ",stock.get(p_no)," jäljellä!")
            print()
        else:
            print("Pahoittelut, Tuotetta ei ole valikoimassamme!")
            print()
        
    elif(c=="P" or c=="p"):# Lainaa tuote
        print()
        p_no = int(input("Kirjoita tuotenumero: "))
        if(p_no in unit_price):
            if(flag==1):
                flag=0
            stock_current = stock.get(p_no)
            if(stock_current>0):
                stock_current = stock.get(p_no)
                stock[p_no] = stock_current-1
                item_price = unit_price.get(p_no)
                total_cost = total_cost+item_price
                print(description.get(p_no),"lisätty tuote lainauslistaan: ","€",item_price)
                cart.append(p_no)# Lisää tuotteen lainauslistaan
            else:
                print("Valitettavasti tuotetta ei ole varastossa tällä hetkellä!")
        else:
                print("Pahoittelut, Tuotetta ei ole valikoimassamme!")
        print()
        
    elif(c=="V" or c=="v"):# Vahvistus
        print()
        print("Lainasit seuraavat tuotteet: ",cart)
        print("Yhteensä: ","€",round(total_cost,2))
        tax= round(0.13*total_cost,2)
        print("ALV. 24%: ","€",tax)
        total = round(total_cost+tax,2)
        print("Verollinen hinta: ","€",total)
        total_cost=0
        flag=1
        print()
        print("Lainaus vahvistettu, lainauslistasi on nollattu. Poistuaksesi paina q")
        print()
        
    elif(c=="Valikko" or c=="valikko"):# Näytä kaikki toiminnot
        print()
        print("Ohjelman Toiminnot")
        print("A - Lisää (inventoi) tuote saldoille")
        print("R - Poista (inventoi) tuote saldoilta")
        print("E - Muokkaa tuotteen tietoja")
        print("L - Listaa kaikki tuotteet")
        print("I - Näytä tuotteen tiedot")
        print("P - Lainaa")
        print("V - Vahvista lainaus")
        print("S - Näytä kaikki lainattavat tuotteet")
        print("Poista - Poista tuote lainaslistalta")
        print("Valikko - Tämä valikko uudelleen") # Mahdollisesti tulee käyttövirheitä kirjoittaessa "valikko" tai "v" joilla on eri toiminnot
        print("Tämä ohjelma on vielä kehitysvaiheessa ja tähän tulee vielä muutoksia.")
        print()
        
    elif(c=="poista" or c=="Poista"):# Poista tuote lainauslistalta
        print()
        are_you_sure = input("Haluatko varmasti poistaa tuotteen lainauslistalta (k/e)? ")
        if(are_you_sure=="k"):
            p_no = int(input("Syötä osakoodi poistaaksesi tuote lainaslistalta: "))
            if(p_no in cart):
                stock_current = stock.get(p_no)
                stock[p_no] = stock_current+1
                item_price = unit_price.get(p_no)
                total_cost = total_cost-item_price
                j=0
                for i in range(0,len(cart)):#
                    if(i==p_no):
                        j=i

                cart.pop(j)
                print(description.get(p_no),"poistettu tuote lainauslistalta: ")
                print()
            else:
                print()
                print("Tuotetta ei ole valittu!")
                print()
                
    elif(c=="s" or c=="S"):#Tulosta lainauslista
        print()
        print(cart)
        print()
        
    else:
        print()
        print("Virhe, Kirjoita help nähdäksesi toiminnot ")
        print()



if(total_cost>0 and flag==0):
    print()
    print("Lainasit: ",cart)
    print("Yhteensä: ","€",round(total_cost,2))
    tax= round(0.13*total_cost,2)
    print("ALV. 24%: ","€",tax)
    total = round(total_cost+tax,2)
    print("Verollinen hinta: ","€",total)
    
print()
print("Hyvää päivänjatkoa")


# TODO: korjaa alla oleva koodi. Pyyhkii tiedoston tyhjäksi
# Kirjoita päivitetty inventaario tiedostoon
# details = open("saldo.txt","w")
# no_items=len(unit_price)
# details.write(str(no_items)+"\n")
# for i in range(0,no_items):
#     details.write(str(i+1)+"#"+str(unit_price[i+1])+"\n")
    
# for i in range(0,no_items):
#     details.write(str(i+1)+"#"+description[i+1]+"\n")
    
# for i in range(0,no_items):
#     details.write(str(i+1)+"#"+str(stock[i+1])+"\n")
    
# details.close()
