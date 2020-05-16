import random

class Personnage :
    def __init__ (self, nom, prenom, age):
        self.nom = nom
        self.prenom = prenom
        self.age = age
        self.mood = "normal"
        self.pv = 100
        print (self.prenom + " entre sur scene ")

    def dit(self, texte):
        if self.mood != "normal" :
            print ("[" + self.mood +"] " + self.prenom + " dit : "+texte)
        else :
            print(self.prenom + " dit : "+texte)

    def etat(self, mood):
        self.mood = mood
        print ("<" +self.prenom + " est " + mood + ">")

    def subit(self, degats):
        self.pv = self.pv - degats
        if self.pv < 0:
            self.pv = 0
    
    def patate(self, dest):
        degats = random.randrange(0, 70)
        dest.subit(degats)
        dest.mood = "normal"
        print("<" + self.prenom + " met une patate de forain a "+ dest.prenom + " et lui inflige " + str(degats) + " pv de degats>")
        dest.dit("Arggg!")

    def highkick(self, dest) :
        degats = random.randrange (0, 50)
        dest.subit(degats)
        print("<" + self.prenom + " met un highkick de batard a "+ dest.prenom + " et lui inflige " + str(degats) + " pv de degats>")
        dest.dit("Ouch!")

    def balayette (self, dest) :
        degats = random.randrange (0, 20)
        dest.subit(degats)
        print("<" + self.prenom + " met une layette lazer de feuj a "+ dest.prenom + " et lui inflige " + str(degats) + " pv de degats>")
        dest.dit("Aie!")

    def direct (self, dest) :
        degats = random.randrange (20, 30)
        dest.subit(degats)
        print("<" + self.prenom + " met un direct du droit a "+ dest.prenom + " et lui inflige " + str(degats) + " pv de degats>")
        dest.dit("Ich!")
    
    def miss (self, dest) :
        print (self.prenom +" rate son attaque!")

    def fatality (self, dest) :
        finish = random.randrange(0, 3)
        finishArray = list([
            self.prenom + " empoigne la television du salon et passe la tete de " +dest.prenom +" au travers", 
            self.prenom + " lance un kamehameha ultime est propulse directement " +dest.prenom +" dans le ciel", 
            self.prenom + " attrape Tornade, lui chatouille le zgeg  et l'enfonce dans le cul de " + dest.prenom, 
            self.prenom + " prends " +dest.prenom +" et l'envoie dans l'atelier, a grand coup de pompes dans le boule et l'atelier s'effondre, comme c'etait previsible "
        ])
        print( "Fatality !!!!")
        print(finishArray[finish])
        
Mathieu = Personnage("Louais", "Mathieu", 25)
Catherine = Personnage("Meyer-bor", "Catherine", 60)

Catherine.dit(Mathieu.prenom + " ferme la putin de fenetre")
Mathieu.dit ("oui " + Catherine.prenom)
Catherine.dit ("Apres "+ str(Mathieu.age)+ " ans tu comprends toujours pas")
Mathieu.dit("Tu me gonfle maman")
Catherine.etat("colere")
Catherine.dit("Prends tes affaires et va chez Clement")
Mathieu.etat("triste")
Mathieu.dit("J'ai plus de chemises pour aller travailler")
Catherine.dit("Et en plus tu me prend pour ta bonne !!")
Catherine.patate(Mathieu)

if Mathieu.pv >= 80 :
    Mathieu.dit("OUINNNN!")
elif Mathieu.pv >= 60 :
    Mathieu.etat("Colere")
    Mathieu.patate(Catherine)
    print("<Un combat epique demarre entre " + Catherine.prenom +" et "+Mathieu.prenom +">")
else :
    Mathieu.etat("mal en point")

toggle = 0

while Mathieu.pv > 0 and Catherine.pv > 0 :
    coup = random.randrange(0, 4)
    if toggle == 0 :
        toggle = 1
        if coup == 0:
            Mathieu.patate(Catherine)
        if coup == 1:
            Mathieu.highkick(Catherine)
        if coup == 2:
            Mathieu.balayette(Catherine)
        if coup == 3:
            Mathieu.direct(Catherine)
        if coup == 4:
            Mathieu.miss(Catherine)
        print("Il reste "+ str(Catherine.pv)+" PV a Catherine")
    elif toggle == 1 :
        toggle = 0
        if coup == 0:
            Catherine.patate(Mathieu)
        if coup == 1:
            Catherine.highkick(Mathieu)
        if coup == 2:
            Catherine.balayette(Mathieu)
        if coup == 3:
            Catherine.direct(Mathieu)
        if coup == 4:
            Catherine.miss(Mathieu)
        print("Il reste "+ str(Mathieu.pv)+ " PV a Mathieu")

if Catherine.pv == 0:
  Mathieu.fatality(Catherine)
if Mathieu.pv == 0:
  Catherine.fatality(Mathieu)

   

   






