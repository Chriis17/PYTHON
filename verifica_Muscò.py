#Senza l'uso delle risorse

class Articolo: 
  def __init__(self, codice, fornitore, marca,prezzo, quantita):
    #1 Implementa il costruttore
    self.codice=codice
    self.fornitore=fornitore
    self.marca=marca
    self.prezzo=prezzo
    self.quantita=quantita


  def scheda_articolo(self):
    #2 Ritorna una stringa contenente gli attributi dell'articolo
    return f"Codice: {self.codice}\nFornitore: {self.fornitore}\nMarca: {self.marca}\nPrezzo: {self.prezzo}\nQuantità: {self.quantita}"

  def modifica_scheda(self):
    #3 Permette di modificare gli attributi dell'articolo
    scelta=0
    while(scelta<1 or scelta>4):
        scelta=int(input("Quale attributo vuoi modificare? (1-Fornitore 2-Marca 3-Prezzo 4-Quantità)"))
    if scelta==1:
      self.fornitore=input("Inserire il nuovo fornitore: ")
    elif scelta==2:
      self.marca=input("Inserire la nuova marca: ")
    elif scelta==3: 
      self.prezzo=int(input("Inserire il nuovo prezzo: "))
    elif scelta==4:
      self.quantita=int(input("Inserire la nuova quantità: "))

#9:26 Invernizzi
      
class Televisore(Articolo):
    def __init__(self, codice, fornitore,marca,prezzo,quantita,pollici,tipo):
      #4 Implementa il costruttore
      super().__init__(codice,fornitore,marca,prezzo,quantita)
      self.pollici=pollici
      self.tipo=tipo

    def scheda_articolo(self):
      #5 Ritorna una stringa contenente gli attributi del televisore
      return super().scheda_articolo()+f"\nPollici: {self.pollici}\nTipo: {self.tipo}"
    
#9:32 Invernizzi
    
class Frigorifero(Articolo):
  def __init__(self, codice, fornitore, marca, prezzo, quantita,dimensioni,modello):
    #6 Implementa il costruttore
    super().__init__(codice,fornitore,marca,prezzo,quantita)
    self.dimensioni=dimensioni
    self.modello=modello

  def scheda_articolo(self):
    #7 Ritorna una stringa contenente gli attributi del frigorifero
    return super().scheda_articolo()+f"\nDimensioni: {self.dimensioni}\nModello: {self.modello}"
  
#9:34 Invernizzi


t1 = Televisore(1,"Fornitore 1","Sony",700,10,40,"Schermo piatto")
print(t1.scheda_articolo())
t1.modifica_scheda()
print(t1.scheda_articolo())



class Ordine():
  def __init__(self,codice,data, piva,indirizzo):
    #8 Implementa il costruttore
    self.codice=codice
    self.data=data
    self.piva=piva
    self.indirizzo=indirizzo
    self.articoli=[]

  def aggiungi_articolo(self,articolo):
    if isinstance(articolo,Televisore):
      tipo_articolo="televisore"
    elif isinstance(articolo,Frigorifero):
      tipo_articolo="frigorifero"
    #9 Completa il metodo aggiungendo l'oggetto alla lista e stampando il messaggio opportuno
    if not articolo in self.articoli:
        self.articoli.append(articolo)
        print(f"{tipo_articolo} aggiunto alla lista")
    else:
        print("Articolo già presente nella lista")
    

  def rimuovi_articolo(self,articolo):
    #10 Implementa il metodo
    if len(self.articoli)>0:
        if isinstance(articolo,Televisore):
            tipo_articolo="televisore"
        elif isinstance(articolo,Frigorifero):
            tipo_articolo="frigorifero"
        if articolo in self.articoli:
            self.articoli.remove(articolo)
            print(f"{tipo_articolo} rimosso dalla lista")
        else:
           print("Articolo inesistente")
    else:
      print("Lista vuota")

  def importo_ordine(self):
    tot=0
    #11 Stampa il numero di articoli e per ogni articolo l'importo (prezzo*quantita)
    print(f"Il numero di articoli presenti nell'ordine è {len(self.articoli)}")
    for articolo in self.articoli:
      tot+=(articolo.prezzo*articolo.quantita)
    print(f"L'importo totale dell'ordine è di {tot} euro")

  def dettaglio_ordine(self):
    #12 Stampa i dettagli dell'ordine e restituisce una lista contenente
    # [somma importi televisori, somma importi frigoriferi, somma importi totali ]
    #...
    sommaF=0
    sommaT=0
    for articolo in self.articoli:
        if isinstance(articolo,Televisore):
            sommaT+=(articolo.prezzo*articolo.quantita)
            tipo_articolo="televisori"
        elif isinstance(articolo,Frigorifero):
            sommaF+=(articolo.prezzo*articolo.quantita)
            tipo_articolo="frigoriferi"
        print(f"Articolo: {tipo_articolo}")
        print(f"Importo = {articolo.prezzo*articolo.quantita}")
        print(articolo.scheda_articolo())
        print()
    return([sommaT,sommaF,sommaT+sommaF])

#10:10 Invernizzi

t2 = Televisore(2,"Fornitore 2","Samsung",1000,5,80,"Schermo curvo")
f1 = Frigorifero(3,"Fornitore 3","Bosch",750,12,'790x2000x600','Ultra')
f2 = Frigorifero(4,"Fornitore 4","Ariston",550,10,'590x1600x500','Medium')

ordine1=Ordine(1,"24/02/2022",'213143','Via della consegna 1')
ordine1.aggiungi_articolo(t1)
ordine1.aggiungi_articolo(t2)
ordine1.aggiungi_articolo(f1)
ordine1.aggiungi_articolo(f2)
print()
ordine1.rimuovi_articolo(f2)
ordine1.rimuovi_articolo(f2)
print()
ordine1.importo_ordine()
print()
importi=ordine1.dettaglio_ordine()
print("--------------------------")
print(f"\nImporto televisori= {importi[0]}")
print(f"\nImporto frigoriferi= {importi[1]}")
print(f"\nImporto totale= {importi[2]}")
print()

class Ordini():
  def __init__(self,nome_negozio,codice_negozio):
    #16 Implementa il costruttore
    self.nome_negozio=nome_negozio
    self.codice_negozio=codice_negozio
    self.ordini=[]


  def aggiungi_ordine(self,ordine):
    #17 Implementa il metodo
    if not ordine in self.ordini:
        self.ordini.append(ordine)
        print("Ordine aggiunto alla lista")
    else:
        print("Ordine già presente nella lista")

  def rimuovi_ordine(self,ordine):
    #18 Implementa il metodo
    if ordine in self.ordini:
        self.ordini.remove(ordine)
        print("Ordine rimosso alla lista")
    else:
        print("Ordine inesistente")

  def totale_ordini(self):
    #19 Implementa il metodo
    #...
    tot=0
    totF=0
    totT=0

    for ordine in self.ordini:
       tupla=ordine.dettaglio_ordine()
       totT+=tupla[0]
       totF+=tupla[1]
       tot+=tupla[2]
    return ([totT,totF,tot])

# 10:33 


ordini_negozio=Ordini("Megastore vendita ",1)
ordini_negozio.aggiungi_ordine(ordine1)
ordini_negozio.rimuovi_ordine(ordine1)
ordini_negozio.rimuovi_ordine(ordine1)

ordini_negozio.aggiungi_ordine(ordine1)

t3 = Televisore(5,"Fornitore 5","LG",600,4,70,"Schermo curvo")
f3 = Frigorifero(6,"Fornitore 6","Bosch",450,10,'490x1000x400','Small')
ordine2=Ordine(2,"25/02/2022",'213113','Via della consegna 2')
ordine2.aggiungi_articolo(t3)
ordine2.aggiungi_articolo(f3)

ordini_negozio.aggiungi_ordine(ordine2)
print()
importiTotali=ordini_negozio.totale_ordini()
print("--------------------------")
print(f"\nImporto totale televisori= {importiTotali[0]}")
print(f"\nImporto totale frigoriferi= {importiTotali[1]}")
print(f"\nImporto totale tutti gli ordini= {importiTotali[2]}")

