class Colis :
    def __init__ (element, id = 0, poids = 0, valeur = 0, rapport=0.0) :
        element.id = id
        element.poids = poids
        element.valeur = valeur
        element.rapport = rapport
    def __print__ (element):
        print "id = ", element.id, " rapport = ", element.rapport
        
def comparePoids(e1, e2):
    if e1.rapport > e2.rapport:
        return -1
    else:
        return 1
    
def fusion (lg,ld) :
    lt = []
    leng = len(lg)
    lend = len(ld)
    i = 0
    j = 0
    while i<leng and j<lend :
        if lg[i].rapport < ld[j].rapport :
            lt.append(lg[i])
            i += 1
        else :
            lt.append(ld[j])
            j+=1
    if i==leng :
        lt.extend(ld[j:])
    else :
        lt.extend(lg[i:])
    return lt


def tri (List) :
    if len(List) <= 1 :
        return List
    milieu = len(List)/2
    lgauche = tri(List[:(milieu)])
   # print lgauche
    ldroite = tri(List[milieu:])
   # print ldroite
    return fusion(lgauche, ldroite)
    
#MAIN
ListColis = []
Debug = raw_input ("Voulez vous executer en mode debug ? o/n : ")
MonFlux = open ("./generateur aleatoire/fichier-colis1.txt", "r")


## Recuperation de la charge max du camion
##MonFlux.readline()
chargeMax = int(MonFlux.readline())
if Debug[0] == 'o' :
    print "Charge maximale admise du camion : ", chargeMax
#MonFlux.readline()

## Extraction des colis dans le fichier source
ligne = MonFlux.readline()
while ligne:
    numbers = map(int, ligne.split())
    ligne = MonFlux.readline()
    if Debug[0] == 'o' :
        print numbers
    c = Colis(numbers[0], numbers[1], numbers[2])
    c.rapport = float(c.valeur) / c.poids
    if Debug[0] == 'o' :
        print "id = ", c.id, " rapport = ", c.rapport
    ListColis.append(c)
    
if Debug[0] == 'o' :
    print "Liste des colis construite après lecture du fichier source"

if Debug[0] == 'o' :
    for colis in ListColis:
        print colis.id, colis.rapport

ListColistri = tri(ListColis)

if Debug[0] == 'o' :
    print "Liste triée :"

    for colis in ListColistri:
        Colis.__print__(colis)

ContenuCamion = []
PoidsEvolution=0
ArgentCamion = 0
for i in range (len(ListColistri)) :
    if PoidsEvolution + ListColistri[i].poids <= chargeMax :
         ContenuCamion.append(ListColistri[i])
         PoidsEvolution += ListColistri[i].poids
         ArgentCamion += ListColistri[i].valeur         
         print "\nOn ajoute le colis # ", ListColistri[i].id
         print "Poids du camion : " ,PoidsEvolution
         print "Argent dans le camion : ", ArgentCamion

print "\nArgent du Camion : " , ArgentCamion, " euros "
print "Poids total : ", PoidsEvolution
    
