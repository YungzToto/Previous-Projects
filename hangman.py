word = 'secret'

allowed_guesses = 5 #The number of guesses you're allowed to have whilst figuring out the word
guesses = [] #List of guessed letters
finished = False

while not finished:
    for letter in word:
        if letter.lower() in guesses: #if the letter is already in guesses (if there's more than one letter)
            print(letter, end = " ")
        else:
            print("_", end = " ")
    
    print("")
    finished = True
    
    #Setting the amount of guesses you have left
    guess = input(f"Allowed Guesses Left: {allowed_guesses}, Next Guess: ")
    guesses.append(guess.lower())
        
    if guess.lower() not in word.lower(): #if the letter is not in the word
        allowed_guesses -= 1 #Reduces the number of guesses you get
        if allowed_guesses == 0:
            break
            
    finished = True #Assuming that the word has already been found until proven otherwise
    
    for letter in word:
        if letter.lower() not in guesses:
            finished = False
            
    if finished:
        print("You have found the word!")
else:
    print("GAME OVER!")
    

            
            
        
