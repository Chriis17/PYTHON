def media_globale(tupla_pluviometrica):
    somma=0
    cont=0
    for città,*dati in tupla_pluviometrica:
        for anno,*mesi in dati:
            if(anno==2023):
                for mese,valore in mesi:
                    if(valore!="N/D"):
                        somma+=valore
                        cont+=1
    if(cont>0):
        return somma/cont
def media(tupla_pluviometrica,m,provincia):
    somma=0
    cont=0
    for città,*dati in tupla_pluviometrica:
        if(città[1]==provincia):
            for anno,*mesi in dati:
                    for mese,valore in mesi:
                        if(valore!="N/D" and m==mese):
                            somma+=valore
                            cont+=1
    if(cont>0):
        return somma/cont
def pioggiaMax(tupla_pluviometrica):
    max=-1
    mesiMax=[]
    cont=0
    cittàMax=[]
    for città,*dati in tupla_pluviometrica:
        if(città[1]=="Milano"):
            for anno,*mesi in dati:
                for mese,valore in mesi:
                    if(valore!="N/D"):
                        cont+=1
                        if(max<valore):
                            cittàMax.clear()
                            mesiMax.clear()
                            max=valore
                            mesiMax.append(mese)
                            cittàMax.append(città[0])
                        elif(max==valore):
                            mesiMax.append(mese)
                            cittàMax.append(città[0])
    if(cont>0):
        return (cittàMax,mesiMax)
def pioggiaMin(tupla_pluviometrica):
    min=1000000
    mesiMin=[]
    cont=0
    for città,*dati in tupla_pluviometrica:
        for anno,*mesi in dati:
            for mese,valore in mesi:
                if(valore!="N/D"):
                    cont+=1
                    if(min>valore):
                        mesiMin.clear()
                        min=valore
                        mesiMin.append(mese)
                    elif(min==valore):
                        mesiMin.append(mese)
    if(cont>0):
        return(mesiMin)
def provinciaPer(tupla_pluviometrica):
    tot=0
    totSo=0
    totMi=0
    totLe=0
    for città,*dati in tupla_pluviometrica:
        for anno,*mesi in dati:
            for mese,valore in mesi:
                if(valore!="N/D"):
                    tot+=valore
    for città,*dati in tupla_pluviometrica:
        for anno,*mesi in dati:
            for mese,valore in mesi:
                if(valore!="N/D"):
                    if(città[1]=="Milano"):
                        totMi+=valore
                    elif(città[1]=="Lecco"):
                        totLe+=valore
                    elif(città[1]=="Sondio"):
                        totSo+=valore
    percMi=(totMi/tot)*100
    percLe=(totLe/tot)*100
    percSo=(totSo/tot)*100
    return(("Milano",percMi),("Lecco",percLe),("Sondio",percSo))
tupla_pluviometrica = (
                      (("Vittuone","Milano"),(2022, ("gennaio",20))),
                      (("Ossona","Milano"),(2023, ("marzo",80))),
                      (("Arluno","Milano"),(2023, ("aprile",60))),
                      (("Corbetta","Milano"),(2023, ("maggio",80))),
                      (("Magenta","Milano"),(2023, ("luglio",30))),
                      (("Casorezzo","Milano"),(2021, ("agosto","N/D"))),
                      (("Varenna","Lecco"),(2023, ("luglio",150))),
                      (("Morbegno","Sondrio"),(2020, ("luglio",165)))
                      )
scelta=0
while(scelta<6):
    scelta=int(input("1)Quantitativo medio di pioggia rilevata nell'anno 2023\n2)Quantitativo medio di pioggia rilevata di una x provincia e un y mese\n3)Città e mese/i più piovoso/i della provincia di Milano\n4)Mese con minor precipitazioni\n5)Percentuale delle precipitazioni per provincia rispetto al totale\n6)Esci\n"))
    if(scelta==1):
        print("La media è ",media_globale(tupla_pluviometrica))
    elif(scelta==2):
        provincia=input("Inserire la provincia da controllare: ")
        mese=input("Inserire il mese da controllare: ")
        print("La media è ",media(tupla_pluviometrica,mese,provincia))
    elif(scelta==3):
        print(pioggiaMax(tupla_pluviometrica))
    elif(scelta==4):
        print(pioggiaMin(tupla_pluviometrica))
    elif(scelta==5):
        print(provinciaPer(tupla_pluviometrica))