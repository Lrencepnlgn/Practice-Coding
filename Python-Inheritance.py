class gukofamily:
    def __init__(db, gukoname, bname, gnname):
        db.fathername = gukoname
        db.mothername = bname
        db.childname = gnname

    def printname(db):
        print(db.fathername, db.mothername, db.childname)

x = gukofamily("Guko", "Bulma", "Gohan")
x.printname()
print("--------------------------------------------")
print("\n")

class gohanfamily:
    def __init__(db, gohanname, videlname, panname):
        db.fathername = gohanname
        db.mothername = videlname
        db.childname = panname

    def printname(db):
        print(db.fathername, db.mothername, db.childname)

x = gohanfamily("Gohan", "Videl", "Pan")
x.printname()
print("--------------------------------------------")
print("\n")

class mrsatenfamily:
    def __init__(db, amaname, anakname,):
        db.fathername = amaname
        db.childname = anakname

    def printname(db):
        print(db.fathername, db.childname)

x = mrsatenfamily("Mr Satan", "Videl")
x.printname()
print("--------------------------------------------")
