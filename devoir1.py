#coding: utf-8

#liste des numéros possibles:
l1 = list(range(30000,100000))
l2 = list(range(00000,18000))
l3 = l1 + l2
buffer = "1"

# Boucle qui ajuste l'affichage, afin qu'il y ait toujours 5 chiffres
for annee in l3 :
    
    #Si l'annee est >= 10 000, on n'ajuste pas l'affichage de la variable annee
    if annee >= 10000:
         print(annee, sep='', end=',')
         
    #Sinon, on ajuste l'affichage en ajoutant les "0" nécessaires
    else :
        if annee < 10000: 
            buffer = "0"
        if annee < 1000:
            buffer = "00"
        if annee < 100:
            buffer = "000"
        if annee < 10 :
            buffer = "0000"
        
        print(buffer, annee, sep='', end=',')
