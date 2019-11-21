
def insert_name():
    name = input("Entrez votre nom:")
    while len(name) == 0:
        print("Vous n'avez pas saisi votre nom")
        name = input("Entrez votre nom:")
insert_name()
