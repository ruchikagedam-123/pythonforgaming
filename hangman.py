import random

# defining function to guess the words
def hangman():
    # Create a list of movie
    word = random.choice(["kabirsingh","race","baghi","superman","thor","pokemon","avengers","rabta"])
    # validate only small alphabets
    validLetetr = "abcdefghijklmnopqrstuvwxyz"
      
    guessmade = ''
    while len(word) > 0:
        main = ""
        missed = 0

        for letter in word:
            if letter in guessmade:
                main = main + letter
            else:
                main = main + "_"+" "
        if main == word:
            print(main)
            print("you win ", name,"!")
            break
        print("Guess the word : ", main)
        guess = input()

        if guess in validLetetr:
            guessmade = guessmade + guess
        else:
            print("Enter a valid character")
            guess = input()
        
        $defining turn for each  
        turns = 10
        
        # If wrong word entered then one turn reduced by one 
        # if all turns are used then it will loose game
        if guess not in word:
            turns = turns -1
            if turns == 9:
                print("9 turns left")
                print("-----------")
                print("      0     ")
            if turns == 8:
                print("8 turns left")
                print("-----------")
                print("      0     ")
                print("      |     ")
            if turns == 7:
                print("7 turns left")
                print("-----------")
                print("      0     ")
                print("      |     ")
                print("     /       ")
            if turns == 6:
                print("6 turns left")
                print("-----------")
                print("      0     ")
                print("      |     ")
                print("     / \     ")
            if turns == 5:
                print("5 turns left")
                print("-----------")
                print("    \ 0     ")
                print("      |     ")
                print("     / \     ")
            if turns == 4:
                print("4 turns left")
                print("-----------")
                print("    \ 0 /   ")
                print("      |     ")
                print("     / \     ")
            if turns == 3:
                print("3 turns left")
                print("-----------")
                print("    \ 0 /|  ")
                print("      |     ")
                print("     / \     ")
            if turns == 2:
                print("2 turns left")
                print("-----------")
                print("      0 _    ")
                print("     /|\     ")
                print("     / \     ")
            if turns == 1:
                print("You loose")
                print("You let a kind man to die")
name = input("Enter Your name  :  ")
print("Welcome", name)
print("Try to guess the word in less than 9 attempt")
hangman()
print()



OUTPUT :
    Enter Your name  :  ruchika
Welcome ruchika
Try to guess the word in less than 9 attempt
Guess the word :  _ _ _ _ _ 
b
Guess the word :  b_ _ _ _ 
a
Guess the word :  ba_ _ _ 
g
Guess the word :  bag_ _ 
h
Guess the word :  bagh_ 
h
Guess the word :  bagh_ 
df
Enter a valid character
u
4 turns left
-----------
    \ 0 /   
      |     
     / \     
Guess the word :  bagh_ 
t
4 turns left
-----------
    \ 0 /   
      |     
     / \     
Guess the word :  bagh_ 
b
Guess the word :  bagh_ 
y
4 turns left
-----------
    \ 0 /   
      |     
     / \     
Guess the word :  bagh_ 
i
baghi
you win ruchika!


Process finished with exit code 0
