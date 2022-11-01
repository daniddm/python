
import random
from turtle import position

word_list = ["baboon", "cebra", "camell"]
chosen_word = random.choice(word_list)
print(chosen_word)



display = []

for x in chosen_word:
    display += "_"


end_of_game = False
lenght = len(chosen_word)
live = 0 

while not end_of_game:
    guess = input("write a letter ? ").lower()
    for i in range(0, lenght):
        letter = chosen_word[i]
        while live < lenght:
            if letter == guess:
                display[i] = letter


        print(f"{''.join(display)}")
    
    if "_" not in display:
        end_of_game = True
        print("you win ")

