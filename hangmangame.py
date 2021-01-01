def hangmangame():
  #Create word list
  import random
  from nltk.corpus import words 

  #Define variables
  word_list = words.words()
  word = random.choice(word_list)
  lives = 8

  #Establishes the position of the entered letter
  def charpos(word, char):
    pos = []
    for i in range(len(word)):
      if word[i] == char:
       pos.append(i)
    return pos

  #Includes the guessed letters among the underscores
  def replacechar(tmpstr, char, pos):
    res = list(tmpstr) 
    for i in pos:
      res[i] = char
    return "".join(res)

  #Let's play hangman and the number of lives is printed at the beginning of the game
  print("Let's Play Hangman!")
  print( "Lives: %d" % lives)
  # just for debug
  #print(word)

  #word_list and lives are self-explanatory
  #blanks = the underscores
  #word = the random word / the answer
  #userinp = the character entered
  #tmpstr = the displayed underscores and letters


  #At the beginning of the game, an amount of underscores that is equal to the number of letters in the answer is printed
  tmpstr = ""
  for i in range(len(word)): 
    tmpstr = tmpstr + "_"
  print (tmpstr)

  i=0

  #Gives instructions on what to do when things happen
  while i in range(len(word)):
    userinp= input("Enter Letter:")
  
    #When the user inputs "Guess Answer", the code asks to input the word. If the word is correct, "You Won" is printed and the game ends, if the word is incorrect, "You Lose" and the correct word are printed, then the game ends 
    if userinp == "Guess Answer": 
      guessinp = input("Enter Answer:")
      if guessinp == word:
        print("You Won!")
        break

      if guessinp != word:
        print("You Lose... The word was: "+ word) 
        break

    #If more than one letters/ characters are entered, a notice is printed and a life is lost
    if len(userinp) != 1 or not(userinp).isalpha():
      print("Please enter a single letter. If you would like to guess the whole word, enter Guess Answer. You have lost one life.")
      continue

    #If the entered letter is in the word, "Correct" and the underscored word are printed, and i is incremented
    if userinp in word:
      pos = charpos(word, userinp)
      tmpstr = replacechar(tmpstr, userinp, pos)
      print("Correct! " + tmpstr)
      i = i+1

   #When the guessed letter is incorrect, "Incorrect" and the remaining lives are printed, one life is subtracted
    else:
      lives = lives-1
      print("Letter not found... Lives Remaining: %d" % lives)
  
    #When the lives run out, "You Lose" is printed along with the answer and the game ends
    if lives == 0:
        print("Out of lives, game over... The word was: "+ word) 
        playagain = input("Play again? (Yes/No )") 
        if playagain == "Yes":
          hangmangame()
        elif playagain == "No":
         break
        else:  
          print("Invalid Input")
          playagain = input("Play again? (Yes/No )") 
    
    #When all of the underscores are replaced and the underscored word matches the answer, "You Won" is printed and the game ends  
    if tmpstr == word:
      print("You Won!")
      break



  #Writes a function that includes the guessed letters among the underscores
  def replacechar(tmpstr, char, pos):
    res = list(tmpstr) 
    res[userinp]= userinp

hangmangame()