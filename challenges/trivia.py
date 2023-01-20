#!/usr/bin/env python3
"""Friday Warmup | Returning Data From Complex JSON"""

import requests
import html

URL= "https://opentdb.com/api.php?amount=3&category=12&difficulty=easy&type=multiple"

def main():
    #input from user to start trivia game
    game_start = input("Would you like to play trivia game?(Y/N): ")

    # data will be a python dictionary rendered from your API link's JSON!
    if game_start.lower() == "y":
        data = requests.get(URL).json()
        print("Question 1:", html.unescape(data["results"][0]["question"]))
        print(data["results"][0]["incorrect_answers"])
        print("\nCorrect Answer:")
        print(data["results"][0]["correct_answer"])
        print("\nNext question - \n")

        print("Question 2:", html.unescape(data["results"][1]["question"]))
        print(data["results"][1]["incorrect_answers"])
        print("\nCorrect Answer:")
        print(data["results"][1]["correct_answer"])
        print("\nLast question - \n")

        print("Question 3:", html.unescape(data["results"][2]["question"]))
        print(data["results"][2]["incorrect_answers"])
        print("\nCorrect Answer:")
        print(data["results"][2]["correct_answer"])
        print("\nThanks for playing!!!")
    elif game_start.lower() == "n":
        print("See you next time!")

if __name__ == "__main__":
    main()
