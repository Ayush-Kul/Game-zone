import random
import pymysql
import matplotlib.pyplot as plt
import numpy as np
connection=pymysql.connect("localhost","root","root","test")
cursor=connection.cursor()
print ("Good Morning, can I know your name please")
Name=input()
games = 0
won = 0
lost = 0
tie = 0
def hangman(a):
  global lost,won
  word=random.choice(a)
  nom=len(word)  
  print("The word has ",nom," letters")
  turns=3
  guesses=''
  while turns>0:
    failed=0
    for char in word:
      if char in guesses:
        print(char, end='')
      else:
        print(' _ ',end='')
        failed+=1
    if (failed==0):
      print("You won!")
      print("The word is ",word)
      won+=1
      break;
    guess=input("\nGuess a character ")
    if guess in guesses:
      print("Already used choose another letter")
      turns!= turns-1
    if guess not in word and guess not in guesses:
      turns-=1
      print("Wrong Guess")
    guesses+=guess
    print("You have ",turns," guesses left")
  if(turns==0):  
    print("You lose, Sorry")
    print("The word is ",word)
    lost+=1
while ('true'):
  game=int(input("Enter \n 1 for Hangman \n 2 For Stone Paper Scissor \n 3 To play a test your luck game \n 4 To stop \n"))
  if(game==1):
    print("Let's begin the game of hangman",Name)
    topic=int(input("Enter \n 1 For Scientific terms \n 2 For English Movies \n 3 for Computer terms"))
    if(topic==1):
      print("You have chosen Scientific terms")
      wordss=['telescope','astronomy','geology','fossil','genetics']
      hangman(wordss)
      games+=1
    elif(topic==2):
      print("You have chosen English Movies")
      wordsm=['titanic','twilight','godzilla','conjuring','spiderman']
      hangman(wordsm)
      games+=1
    elif(topic==3):
      print("You have chosen Computer terms")
      wordsip=['analog','cache','database','emoticon']
      hangman(wordsip)
      games+=1
    else:
      print("Wrong choice")
  elif(game==2):
    choice = "Y"
    array=["Rock","Paper","Scissor"]
    while choice != 'N':
      ans = int(input('Enter 1-Rock 2-Paper 3-Scissor : '))
      comp = random.randint(1, 3)
      print ("The computer choose",array[comp-1])
      if ans == comp:
         print("Tie!!!")
         tie += 1
      elif ans == 1:
         if(comp == 3):
             print("You won")
             won += 1
         elif(comp == 2):
             print("You lost")
             lost += 1
      elif(ans == 2):
          if(comp == 1):
             print("You won")
             won += 1
          elif(comp == 3):
             print("You lost")
             lost += 1
      elif(ans == 3):
         if(comp == 2):
             print("You won")
             won += 1
         elif(comp == 1):
             print("You lost")
             lost += 1
      else :
        print("Wrong Input")
      games += 1
      choice = input("Want to play more( Y/N) :").upper()
  elif(game==3):
    guessestaken=0
    turn=3
    number=random.randint(1,10)
    print('Well, ' + Name + '  I am thinking of a number between 1 and 10.')
    while (guessestaken<3):
        print('Take a guess.You have 3 turns.')
        guess = input()
        guess = int(guess)
        guessestaken=guessestaken+1
        if (guess<number):
            print("Your guess is low")
            turn-=1
        elif (guess>number):
            print("Your guess is high")
        elif (guess==number):
            break
    if(guess==number):
        guessestaken=str(guessestaken)
        print('Good job,'+Name+'! You guessed my number in '+ guessestaken +' guesses!')
        won+=1
    else:
        number=str(number)
        print("No. The number I was thinking of was"+ number)
        lost+=1
  elif(game==4):
    break
print('\n\n\n Simple stat of this Game for',Name,' \n')
print(' Total Games  :', games)
print("You won Games :", won)
print("You lost Games :", lost)
print("Tie Games :", tie)
headings=[ 'Won','Lost','Tie']
scores=[won,lost,tie]
c=['g','r','b']
plt.pie(scores,labels=headings,colors=c,autopct="%6.2f%%")
plt.show()
values=(Name,won,lost,tie,games)
st="insert into scoreboard(Name,Games_won,Games_lost,Games_tied,Games_played) values(%s,%s,%s,%s,%s)"
ab=cursor.execute(st,values)
connection.commit()
if(ab==1):
  print("Your scores have been recorded. Thank you for playing.")
    
    
  

