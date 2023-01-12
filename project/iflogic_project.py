#!usr/bin/env python3
import random
import time

def main():

    #list of hogwart houses
    hogwart_houses = ["Gryffindor", "Hufflepuff", "Ravenclaw", "Slytherin"]
       
    game_start = 'True';

    #welcome message to game
    print("Welcome one and all to the Hogwart's House sorting game.\nIt's time to find out what house you will be joining.\nThere's nothing left to fear. Answer all questions and you'll find the right place.\nWho knows - your house may surprise you...\n")

    while game_start == "True":

    #first question of game - discusses pets
        first_question = input("Question 1: What animal would you choose as a pet? (Lizard, Dog, Cat, or Ferret): ")
    
    #if/elif/else statements for first question
        if first_question.lower() == "lizard":
            print("Reptilian response. Interesting.\n")
        elif first_question.lower() == "dog":
            print("Barktastic answer.\n")
        elif first_question.lower() == "cat":
            print("Cat person. Purrrfect.\n")
        elif first_question.lower() == "ferret":
            print("Ferret? Ha!.\n")
        else:
            print("Very naughty. You didn't choose an animal from the list. We shall see what your other answers reveal about you.\n")
        
    #second question of game - discusses class topics
        second_question = input("Question 2: Pick a class that sounds interesting (Charms, Potions, Magic, Transfiguration): ")
    
    #if/elif/else statements for second question
        if second_question.lower() == "charms":
            print("Charms. How quaint.\n")
        elif second_question.lower() == "potions":
            print("Concoctions galore.\n")
        elif second_question.lower() == "magic":
            print("Who doesn't love magic?!\n")
        elif second_question.lower() == "transfiguration":
            print("Shape-shifter eh? Good stuff.\n")
        else:
            print("Still being defiant. Tsk tsk.\n")
    
    #print statement letting user know last question is coming
        print("Last question!\n")
    
    #third question of game - asks user to pick a color
        third_question = input("Question 3: Pick a color (Pink, Purple, White, Orange): ")

    #if/elif/else statement for third question
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
    
        print("It's decision time. you belong to House...")

    #while loop that performs a countdown from 5 to 1
        countdown = 5
        while countdown > 0:
            print(countdown)
            time.sleep(1)
            countdown = countdown - 1  
        print(random.choice(hogwart_houses),"!")

        game_restart = input("\nWant to try again to get another house? (Yes, No): ")
    
        if game_restart.lower() != "yes": 
            game_start = 'False';
            print("See you next time!")


if __name__ == "__main__":
    main()

