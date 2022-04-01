import random
import nltk
nltk.download('wordnet')
nltk.download('omw-1.4')
from nltk.corpus import wordnet 

# Start Menu
print('Welcome to Hangman!!\n')
diff = input('''Choose your difficulty(1-4):
             1. Easy
             2. Medium
             3. Hard
             4. Flawless\nDifficulty: ''')

try:
  from nltk.corpus import words as nltk_words
  word = (random.choice(nltk_words.words())).lower()
except:
  nltk.download('words')
  from nltk.corpus import words as nltk_words
  word = (random.choice(nltk_words.words())).lower()

# Setting Difficulties
if '1' in diff:
  while len(word) > 5:
    word = random.choice(nltk_words.words())
elif '2' in diff:
  while len(word) < 5 or len(word) > 10:
    word = random.choice(nltk_words.words())
elif '3' in diff or '4' in diff:
  while 10 >= len(word):
    word = random.choice(nltk_words.words())

# Game Conditions Setup
print(f'\n\nThe word\'s length is {len(word)}')
game = False
tries = 0
wrong = []
def split(word):
    return [char for char in word]
split = split(word)
right = []
for x in split:
  right.append('-')

# def retry():
#   print(f'Tries: {wrong}')
#   guess = input('\nGuess a letter!: ')
  
while game == False:
  print(f'Tries: {wrong}, \nWord so far: {right}')
  guess = input('\nGuess a letter!: ')
  
  # Setting Gameplay
  if guess in wrong or guess in right:
    print('You have already tried this letter!')
    
  else:
    tries += 1
    ln = 0
    if guess in word:
        for l in word:
          if l == guess:
            ln += 1
  
        if ln > 1:
          print(f'\nYup, appears {ln} times!')
          for i, character in enumerate(split):
            if character == guess:
              right[i] =  character     
        else:
          print('\nYup!')
          for i in split:
              if i == guess:
                pos = split.index(i)
                right[pos] = guess
                
    else:
      if '4' in diff:
        win = False
        game = True
      else:
        print('\nWrong!')
        wrong.append(guess)
  
  progress = 0
    
  for i in split:
    if i in right:
      progress += 1
  if progress == len(word): 
    win = True
    game = True
  if tries > (len(word) + 5):
    win = False
    game = True

if win == True:
  print('\nCorrect! Congratulations!')
else:
  print('Tough luck! Maybe next time :)')

print('\nThe word was ' + word)
# print('*Definition Pending*...')
# syns = wordnet.synsets(word)[0]
# print(syns)
# print(f'\n\n{word}: {syns.definition()}')
# We pretend all this doesn't exist