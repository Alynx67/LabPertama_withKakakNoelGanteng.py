Hidden_word = "sixseven"
Word_guess = []
Chances = 5

print ("Brainrot Hangman Quiz")

while Chances > 0:
    Shown_word = ""

    for word in Hidden_word:
        if word in Word_guess:
            Shown_word= word 
        else :
            Shown_word += "_"
    print ("Word:", Shown_word)
    print("Remaining lives", Chances)
    
    if "_" not in Shown_word:
        print("Passed")
        break
    
    Guess = input("Input 1 word:").lower()
    
    if len(Guess) != 1 or not Guess.isalpha():
        print("Only input 1 word")
        continue
    if Guess in Word_guess:
        print("This word have been chosen")
        continue 
    Word_guess.append(Guess)
    Chances -= 1

if Chances == 0:
    print("The End")
    print ("Correct word is", Hidden_word)