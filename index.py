#import functions
import random
import hangman_word_list

#logo
logo = ''' 
😀    😁    😂    🤣    😃    😄    😎  
 _                                            
| |                                            
| |__   __ _ _ __   __ _ _ __ ___   __ _ _ __  
| '_ \ / _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
| | | | (_| | | | | (_| | | | | | | (_| | | | |
|_| |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
  😍                __/ |    🥰  🤗   🤩   🤔                 
                   |___/    '''

#stages
stages = ['''
  +---+
  |   |
 😭   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
 😱   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
 😨   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
 😓   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
 😥   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
 🥲    |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']

#print logo
print(logo)

#chosen word
chosen_word = random.choice(hangman_word_list.word_list)

# no. of display blanks
display = []
for i in chosen_word:
    display+= "_"

# no of lives
lives = 6

# for stoping the while loop
end_of_game = False


while not end_of_game:

    # guess letter
    guess = input("Guess a letter ").lower()

    # putting guess letter in display
    for position in range(len(chosen_word)):
        letter = chosen_word[position]
        if letter == guess:
            display[position] = letter
    
    print(display)

    # lives game
    if guess not in chosen_word:
        lives -=1
        print(stages[lives])
        print(f"your guesses letter {guess} is not in chosen word")
        if lives == 0:
            end_of_game = True
            print("you lose")

    # winning game condition
    if "_" not in display:
        end_of_game = True
        print("You Win")

# improving UI    
if guess in display:
    print("you alredy guess a latter")



