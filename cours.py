
#variable base
phone="02.02.02.02.02"
reponse = input("Tapez entrée pour connaitre une autre citation, ou B pour quitter le programme.")
#liste (array)
quotes = ["Ecoutez-moi, Monsieur Shakespeare, nous avons beau être ou ne pas être, nous sommes !", "On doit pouvoir choisir entre s'écouter parler et se faire entendre."]
perso = ["babare", "zelda"]
#tuple (array avec champs non modifiables)
gps = ("Paris", 522456, 365177, "Londres")
#dictionnaire (tableau avec une valeurs et clefs)
capitale = {"France : Paris", "Angleterre : Londres"}


#conditions

# if reponse == "B":
#   pass
# elif reponse =="C":
#   print("La réponse C")
# else:
#   print("D la réponse D")

#fonction
def citation_random(my_list):
  
  citation = my_list[0]
  return citation

#boucles (while)
while reponse != "B":
  print(citation_random(quotes))
  reponse = input("Tapez entrée pour connaitre une autre citation, ou B pour quitter le programme.")

#boucles (for)
for perso in perso:
  n_perso = perso.capitalize() #mets la première lettre de chaque mots en majuscule
  print(n_perso)





  