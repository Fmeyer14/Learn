

#Cet algorithme doit demander une heure et en afficher une autre. Mais cette fois, il doit gérer également les secondes, 
#et afficher l'heure qu'il sera une seconde plus tard.
#Par exemple, si l'utilisateur tape 21, puis 32, puis 8, l'algorithme doit répondre : "Dans une seconde, il 
#sera 21 heure(s), 32 minute(s) et 9 seconde(s)".
#NB : là encore, on suppose que l'utilisateur entre une date valide.



h = int(input(print("Entrez une heure (valide)")))
m = int(input(print("Entrez les minutes (valides)")))
s = int(input(print("Entrez les secondes (valide)")))
s = s + 1 #Ici vous pouvez changer le nombre de secondes à rajouter ou tous simplemnt en la remplaçant par une variable 

if s == 60:
   s = 0
   m = m + 1

if m == 60 :
   m =0
   h = h+1

if h == 24:
   h =0

print("Dans une seconde il sera ",h ,":",m,":",s)
