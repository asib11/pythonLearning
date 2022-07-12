import random

HANG_PICS = ['''
                    +---+
                        |
                        |
                        |
                       ===''', '''
                   +---+
                   O   |
                       |
                       |
                      ===''', '''
                   +---+
                   O   |
                   |   |
                       |
                      ===''', '''
                   +---+
                   O   |
                  /|   |
                       |
                      ===''', '''
                   +---+
                   O   |
                  /|\  |
                       |
                      ===''', '''
                   +---+
                   O   |
                  /|\  |
                  /    |
                      ===''', '''
                   +---+
                   O   |
                  /|\  |
                  / \  |
                      ===''']

idea_words ='Apples, Apricots, Avocados,Bananas, Boysenberries, Blueberries, Bing Cherry,herries, Cantaloupe, Crab apples, Clementine, Cucumbers,Damson plum, Dinosaur Eggs (Pluots), Dates, Dewberries, Dragon Fruit,Elderberry, Eggfruit, Evergreen Huckleberry, Entawak,Fig, Farkleberry,Grapefruit, Grapes, Gooseberries, Guava,Honeydew melon, Hackberry, Honeycrisp Apples,Jackfruit, Java Apple, Jambolan,Kiwi, Kaffir Lime, Kumquat,Lime, Longan, Lychee, Loquat,Mango,Mandarin Orange, Mulberry, Melon,Nectarine, Navel Orange,Olive, Oranges, Ogeechee Limes, Oval Kumquat,Papaya, Persimmon, Paw Paw, Prickly Pear, Peach, Pomegranate, Pineapple, Passion Fruit,Rambutan, Raspberries, Rose Hips,Star Fruit, Strawberries, Sugar Baby Watermelon,Tomato, Tangerine, Tamarind, Tart Cherries,Ugli Fruit, Uniq Fruit, Ugni,Vanilla Bean, Velvet Pink Banana, Voavanga,Watermelon, Wolfberry, White Mulberry' .split()

def RandomWord(wordList):
    word_index = random.randint(0, len(wordList) - 1)
    return wordList[word_index]

def displayBoard(missed_letter, correct_letter, secret_word):
    print(HANG_PICS[len(missed_letter)])
    print()
    print('Missing letters:', end=' ')
    for letter in missed_letter:
        print(letter, end=' ')
    print()
    blanks = '_' * len(secret_word)
    for j in range(len(secret_word)):
        if secret_word[j] in correct_letter:
            blanks = blanks[:j] + secret_word[j] + blanks[j+1:]


def getGuess(alreadyGuessed):
    while True:
        print('Guess a letter:')
        guess = input()
        guess = guess.lower()
        if len(guess) != 1:
           print('Please enter a single letter.')
        elif guess in alreadyGuessed:
           print('You have already guessed that letter. Please choose again.')
        elif guess not in 'abcdefghijklmnopqrstuvwxyz':
           print('Please enter a letter:')
        else:
           return guess

def AgainPlay():
    print('You want to play again? (yes or no)')
    return input().lower().startswith('y')

print('H A N G M A N   G A M E')
missed_letter = ''
correct_letter = ''
secret_word = RandomWord(idea_words)
game_is_done = False

while True:

      guess = getGuess(missed_letter + correct_letter)
 
      if guess in secret_word:
          print("Right, well done!")
          correct_letter = correct_letter + guess
          foundAllLetters = True
          for k in range(len(secret_word)):
               if secret_word[k] not in correct_letter:
                   foundAllLetters = False
                   break
          if foundAllLetters:
              print('Yes! Secret word is "' + secret_word +'"! You have won!')
              game_is_done = True
      else:
           print(' It is Wrong guess!')
           displayBoard(missed_letter, correct_letter, secret_word)
           missed_letter = missed_letter + guess

      if len(missed_letter) == len(HANG_PICS) - 1:
         displayBoard(missed_letter, correct_letter, secret_word)
         print('You have run out of guesses!\nAfter ' +
                str(len(missed_letter)) + ' missed guesses and ' +
                str(len(correct_letter)) + ' correct guesses,the word was "' + secret_word + '"')
         game_is_done = True

      if game_is_done:
         if AgainPlay():
            missed_letter = ''
            correct_letter = ''
            game_is_done = False
            secret_word = RandomWord(idea_words)
         else:
            break