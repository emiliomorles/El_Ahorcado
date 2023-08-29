#Juego de El Ahorcado en español
import random
import os #it helps cleaning the previous stage
from hangman_words import word_list
from hangman_art import stages, logo

print(logo)
print("EL AHORCADO\n")

chosen_word = random.choice(word_list)
word_length = len(chosen_word)

end_of_game = False
lives = 6

display = []
for _ in range(word_length):
    display += "_"

while not end_of_game:
    guess = input("Adivina una letra: ").lower()

    os.system('cls' if os.name == 'nt' else 'clear') #with this code the game would clean the previous stage

    if guess in display:
        print(f"You already choose the letter {guess}")

    #Check guessed letter
    for position in range(word_length):
        letter = chosen_word[position]
        # print(f"Current position: {position}\n Current letter: {letter}\n Guessed letter: {guess}")
        if letter == guess:
            display[position] = letter
             
    #Check if user is wrong.
    if guess not in chosen_word:       
        lives -= 1
        if lives == 0:
            end_of_game = True
            print("Perdiste.💀")
        print(f"La letra {guess} no esta en la palabra. Pierdes una vida")
    print(f"{' '.join(display)}")

    #Check if user has got all letters.
    if "_" not in display:
        end_of_game = True
        print("¡Ganaste! 😃")

    print(stages[lives])