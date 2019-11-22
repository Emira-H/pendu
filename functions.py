import random
from donnees import liste_mots

def insert_name():
    name = input("Entrez votre nom:")
    while len(name) == 0:
        print("Vous n'avez pas saisi votre nom")
        name = input("Entrez votre nom:")
    return name
insert_name()

def choice_pc():
# lecture from objects contained in file
    word_pc = random.choice(liste_mots)
    print(word_pc)
    length_word_pc = len(word_pc)
    star = "*"
    print(length_word_pc * star)
    return word_pc


def choice_letter():
    word_pc = choice_pc()
    letter = input("Veuillez proposer une lettre ou le mot:")
    letter = str(letter)
    while len(letter) < 1 or len(letter) > len(word_pc):
            letter = input("Veuillez proposer une lettre ou le mot:")
    return letter
