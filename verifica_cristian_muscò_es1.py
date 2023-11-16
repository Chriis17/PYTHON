def media_max_min(nome,tupla):
    cont=0
    max=-1
    min=1000000
    mesiMax=[]
    mesiMin=[]
    tot=0
    for rep,*vett in tupla:
        if(nome==rep):
            for mesi in vett:
                for mese in mesi:
                    if(mese[1]!="N/D"):
                        tot+=mese[1]
                        cont+=1
                        if(max<mese[1]):
                            mesiMax.clear()
                            max=mese[1]
                            mesiMax.append(mese[0])
                        elif(max==mese[1]):
                            mesiMax.append(mese[0])
                        if(min>mese[1]):
                            mesiMin.clear()
                            min=mese[1]
                            mesiMin.append(mese[0])
                        elif(min==mese[1]):
                            mesiMin.append(mese[0])
    if(cont>0):
        return (tot/cont,(max,mesiMax),(min,mesiMin))
            

tupla=(("RepartoA", [("Gennaio",1500),("Febbraio","N/D"), ("Marzo",1000),("Aprile",750),("Maggio","N/D"), ("Giugno",1100)]),
       ("RepartoB", [("Gennaio","N/D"),("Febbraio",1240), ("Marzo",900),("Aprile",300),("Maggio",550), ("Giugno","N/D")]))

nome=input("Inserire il nome del reparto: ")

media_max_min=media_max_min(nome,tupla)
if(media_max_min!=None):
    print("La media delle vendite è",media_max_min[0])
    print("Il/I mese/i in cui si è verificato il maggior ricavo dalle vendite è/sono",media_max_min[1][1],"pari a",media_max_min[1][0],"euro")
    print("Il/I mese/i in cui si è verificato il minor ricavo dalle vendite è/sono",media_max_min[2][1],"pari a",media_max_min[2][0],"euro")
else:
    print("Reparto insesistente")