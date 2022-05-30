import random
from re import A
from hangman_design import *
from words import *

chosen_word = random.choice(word_list)

#run this line for test the code and already know the solution.
#print(f'Pssst, the solution is {chosen_word}.')

display=[]
lives=6

for i in chosen_word:
  display.append('_')

print(logo)
print(display)
print(stages[lives])

while True:
  guess = input("Guess a letter: ").lower()
  for i in range(len(display)):
    if chosen_word[i]==guess:
      display[i]=guess

  if guess not in chosen_word:
    lives-=1
    print(stages[lives])

  if lives==0:
    print('Game Over')
    break
  
  if '_' in display:
    print(display)
  else:
    print(display)
    print('You win') 
    break
