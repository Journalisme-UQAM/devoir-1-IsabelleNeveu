#coding: utf-8

#liste des numéros possibles:
l1 = list(range(30000,100000))
l2 = list(range(00000,18000))
l3 = l1 + l2
# buffer = "1"

# Boucle qui ajuste l'affichage, afin qu'il y ait toujours 5 chiffres
for annee in l3 :
    
    #Si l'annee est >= 10 000, on n'ajuste pas l'affichage de la variable annee
    if annee >= 10000:
         print(annee, sep='', end=',')
         print(annee) ### Mon ajout
         
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

### Mes commentaires sont précédés de 3 «#» pour les distinguer des tiens :)

### Ton script est très bien documenté grâce aux nombreux commentaires que tu y fais
### Tu as imaginé une bonne solution pour contourner l'obstacle du passage à l'an 2000 :)
### Attention à la consistance dans ton code -> parfois il y a un espace avant le deux-points, parfois pas. Il est d'usage de ne pas en mettre.

### Faire plusieurs «if» d'affilée fonctionne, ici, mais n'est pas nécessaire.
### Il aurait été tout aussi bien d'écrire, après un premier «if», «elif» (qui signifie «else if»).
### Quelle est la différence? Dans une série d'«if», le code vérifie toutes les conditions. Avec des «elif», le code vérifie les conditions l'une après l'autre, et dès qu'une est satisfaite, il arrête et ne vérifie pas les suivantes.

### Enfin, il n'était pas nécessaire d'ajouter des séparateurs entre chaque affichage des numéros de permis. C'est bien d'avoir appris cette fonctionnalité, cela dit :)
### L'affichage des numéros sur des lignes distinctes était correct.

        print(buffer + str(annee)) ### Mon ajout