#!usr/bin/env python3

import random

def main():

    hogwart_houses = ["Gryffindor", "Hufflepuff", "Ravenclaw", "Slytherin"]

    print("Welcome one and all to the Hogwart's House sorting game.\nIt's time to find out what house you will be joining.\nThere's nothing left to fear. Answer all questions and you'll find the right place.\nWho knows - your house may surprise you...\n")

    first_question = input("Question 1: What animal would you choose as a pet? (Lizard, Dog, Cat, or Ferret): ")
    
    if first_question.lower() == "lizard":
        print("Reptilian response. Interesting.\n")
    elif first_question.lower() == "dog":
        print("Barktastic answer.\n")
    elif first_question.lower() == "dog":
        print("Cat. Purrrfect.\n")
    elif first_question.lower() == "ferret":
        print("Ferret? Ha!.\n")
    else:
        print("Very naughty. You didn't choose an animal from the list. We shall see what your other answers reveal about you.\n")
        

    second_question = input("Question 2: Pick a class that sounds interesting (Charms, Potions, Magic, Transfiguration): ")

    if second_question.lower() == "charms":
        print("Charms. How quaint.\n")
    elif second_question.lower() == "potions":
        print("Concoctions galore. Continue.\n")
    elif second_question.lower() == "magic":
        print("Who doesn't love magic?!\n")
    elif second_question.lower() == "transfiguration":
        print("Shape-shifter eh? Good stuff.\n")
    else:
        print("Still being defiant. Tsk tsk.\n")

    print("Last question!\n")

    third_question = input("Question 3: Pick a color (Pink, Purple, White, Orange): ")

    if third_question.lower() == "pink":
        print("Of course you chose pink.\n")
    elif third_question.lower() == "purple":
        print("Purple! How majestic!\n")
    elif third_question.lower() == "white":
        print("White? You're a special case.\n")
    elif third_question.lower() == "orange":
        print("Interesting choice. Orange of all colors.\n")
    else:
        print("Guess our color choices aren't good enough. Let's just see where you end up.\n")
    
    print("It's decision time. Countdown Please-")
    
    decision = 3

    while decision > 0:
        print(decision)
        decision = decision - 1

    print("\nYou belong to House...\n")

    print(random.choice(hogwart_houses))

main()

