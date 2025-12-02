from words import words
import random

def hangman():
    hint = random.choice(list(words.keys()))
    secret_word = random.choice(words[hint])
    #print(secret_word)
    lives = 6

    #user guessed letters
    guessed_letters = set()
    print('Hint, The category of the word is: ', hint)

    while lives > 0:
        
        #generate blanks
        blanks = ''
        for letter in secret_word:
            if letter in guessed_letters:
                blanks += letter
            else:
                blanks = blanks + '_'

        print('Word to Guess: ' + blanks)
        print('Guessed letters: ', ', '.join(sorted(guessed_letters)))
        print('Lives', lives)
        
        #check win
        if '_' not in blanks:
            print(f'You Win, The word to guess was {secret_word}')
            return
        
        #user input
        user_input = input('Guess a letter: ').lower()

        if len(user_input) != 1:
            print('Enter A single letter')
            continue
        if user_input in guessed_letters:
            print('You already guessed that letter')
            continue

        guessed_letters.add(user_input)

        #check lives
        if user_input not in secret_word:
            lives -= 1
            print(f'You guessed the wrong letter, you have {lives} left')
    print('You Lost , The word was: ', secret_word)

hangman()


    