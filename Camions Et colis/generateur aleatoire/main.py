import random
nombreColis = random.randint(1,50)
fichierColis = open("fichier-colis1.txt", 'w')
fichierColis.write(str(random.randint(100,1000)))
fichierColis.write("\n")
for i in range(nombreColis):
    fichierColis.write(str(random.randint(1,100)))
    fichierColis.write(" ")
    fichierColis.write(str(random.randint(1,100)))
    fichierColis.write(" ")
    fichierColis.write(str(random.randint(1,100)))
    fichierColis.write("\n")
      
fichierColis.close()


    
    
