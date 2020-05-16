import sys


# https://www.programiz.com/python-programming/user-defined-exception
# if vaut mieux lever des exceptions et les recuperer a un seul point, tu comprendras plus tard ca
class IncorrectInput(Exception):
    pass


class Annuaire:
    def __init__(self):
        self.annuaireArray = []
        try:
            f = open("file.txt", "r")
            self.annuaireArray = f.read().split("\n")
            f.close()
        except IOError:
            # Heu tu devrais laisser un commentaire parce la je comprends pas ce que tu fais
            # C'est pour un probleme de permissions ?
            f = open("file.txt", "x")
            f.close()

    def save(self):
        f = open("file.txt", "w")
        g = "\n".join(self.annuaireArray)
        f.write(g)
        f.close()

    def create(self, nom):
        # strip evite d'avoir des espaces dans ce que tu stocke:
        # ' lol '.strip() -> 'lol'
        self.annuaireArray.append(nom.strip())

    def read(self):
        for nom in self.annuaireArray:
            print(nom)

    def update(self, nom, nom2):
        try:
            self.annuaireArray.remove(nom)
        except Exception:
            # https://realpython.com/python-f-strings/
            raise IncorrectInput(f"{nom} not found")
        else:
            # Si tout se passe bien on ajoute nom2
            self.annuaireArray.append(nom2)

    def delete(self, nom):
        try:
            self.annuaireArray.remove(nom)
            print(self.annuaireArray)
            print("deleted")
        except Exception:
            raise IncorrectInput(f"{nom} not found")


# Par convention une classe est en majuscule mais pas un object
a = Annuaire()

sys.argv.pop(0)


try:
    if len(sys.argv) == 0:
        raise IncorrectInput("Pas le bon nombre d'arguments")
    else:
        if sys.argv[0] == "create":
            if len(sys.argv) >= 2:
                sys.argv.pop(0)
                for nom in sys.argv:
                    a.create(nom)
            else:
                raise IncorrectInput("pas de nom a creer")

        elif sys.argv[0] == "read":
            a.read()

        elif sys.argv[0] == "update":
            if len(sys.argv) >= 3:
                # https://stackoverflow.com/questions/34308337/unpack-list-to-variables
                [_, old, new] = sys.argv
                a.update(old, new)
            else:
                raise IncorrectInput("nombre de parametes pas respecté")

        elif sys.argv[0] == "delete":
            if len(sys.argv) >= 2:
                nom = sys.argv[1]
                a.delete(nom)
            else:
                raise IncorrectInput("nombre de parametes pas respecté")
        else:
            raise IncorrectInput("Enter a valid function")
except IncorrectInput as ex:
    print(ex)

a.save()
