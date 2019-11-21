import random
from donnees import liste_mots

def insert_name():
    name = input("Entrez votre nom:")
    while len(name) == 0:
        print("Vous n'avez pas saisi votre nom")
        name = input("Entrez votre nom:")
insert_name()

def choose_word():

# lecture from objects contained in file
    word_pc = random.choice(liste_mots)
    print(word_pc)
choose_word()
