# class Animal () :

#     def __init__ (self, couleur, cri, nom) :
#         self.couleur = couleur  
#         self.cri = cri
#         self.nom = nom

#     def crier (self) :
#         print(self.cri)
    
# class Mammifere (Animal) :

#     def __init__ (self, couleur, cri, nom, alimentation) :
#         super ().__init__ (couleur, cri, nom) 
#         self.alimentation = alimentation
    
#     def manger (self) :
#         if self.alimentation == "carnivore" :
#             print("Je mange de la viande")
#         elif self.alimentation == "herbivore" :
#             print ("Je mange des vegetaux")



# class Lapin ( Mammifere ) :

#     def meurt (self) :
#         print("aaaargh !")
    
# class Ours ( Mammifere ) :

#     def attaquer (self) :
#         print("graoour")

#     def crier(self) :
#         super().crier()
#         print("kurva")

# panpan = Lapin("Blanc", "ouch", "panpan", "herbivore")
# vladimir = Ours("brun", "Niet", "vladmir", "carnivore")
# vladimir.crier()
# vladimir.manger()
# panpan.manger()
# panpan.meurt()
# panpan.crier()
age = 36
txt = "My name is John, and I am {}"
print(txt.format(age))