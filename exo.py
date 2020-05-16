import sys
import Animal

class Annuaire():
    
    def __init__ (self) :   
        self.annuaireArray =[]
        try:
            f = open("file.txt","r")
            self.annuaireArray = f.read().split('\n')
            f.close()    
        except IOError:
            f = open ("file.txt","x")
            f.close()
            
    def __del__(self) :
        f = open("file.txt", "w")
        g ="\n".join(self.annuaireArray)
        f.write(g)
        f.close()

    def create(self, nom):
        self.annuaireArray.append(nom)

    def read(self, nom):
        for nom in self.annuaireArray:
            print(nom)

    def update(self, nom, nom2):
        try:
            self.annuaireArray.remove(nom)
            self.annuaireArray.append(nom2)
        except:
             print(nom+" not found")
            
    def delete(self, nom):
        try:
            self.annuaireArray.remove(nom)
            print (self.annuaireArray)
        except:
             print(nom+" not found")


A = Annuaire()

sys.argv.pop (0)

def error():
    print("Use ex : exo.py myfunction myparam")

if len(sys.argv) == 0:
    error()
else :
    if sys.argv[0]== "create":
        if len(sys.argv) >= 2:
            sys.argv.pop(0)
            for nom in sys.argv:
                A.create(nom)
        else :
            error()
        
    elif sys.argv[0]== "read" :
        if len(sys.argv) >= 2:
            nom = sys.argv[1]
            A.read(nom)
        else :
            error()

    elif sys.argv[0]=="update" :
        if len(sys.argv) >= 3:
            nom = sys.argv[1]
            nom2 = sys.argv[2]
            A.update(nom, nom2)
        else :
            error()
    
    elif sys.argv[0]=="delete" :
        if len(sys.argv) >= 2:
            nom = sys.argv[1]
            A.delete(nom)
        else :error()
    else :
        print("Enter a valid function")

del A



