h = int(input(print("Entrez une heure (valide)")))
m = int(input(print("Entrez les minutes (valides)")))
s = int(input(print("Entrez les secondes ")))
s = s + 1

if s == 60:
   s = 0
   m = m + 1

if m == 60 :
   m =0
   h = h+1

if h == 24:
    h =0

print("Dans une minute il sera ",h ,":",m,":",s)
