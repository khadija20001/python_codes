import random
import  string
words = ["python", "java", "kotlin", "javascript"]
def valid_input():
    valid = False 
    while valid != True:
      user_input =input("Enter a letter: ").lower()
      if len(user_input)!=1 :
        print("Please enter a single character.")
      elif user_input not in string.ascii_lowercase:
        print("Please enter a lowercase letter.")
      else:
        valid = True
        return user_input

def hangman():
    word = random.choice(words)
    word_letters= set(word) # save the letters in the word
    alphabet = set(string.ascii_lowercase) # save the letters in the alphabet
    # the above line is the same as the line below
    # alphabet = set("abcdefghijklmnopqrstuvwxyz")
    used_letters = set() # save the letters that the user has 
    lives = 6 # number of lives the user has
    print("Welcome to hangman")
    # getting user input
    while len(word_letters) > 0 and lives > 0:
        print("You have", lives, "lives left and you have used these letters: ", " ".join(used_letters))
        user_input=valid_input()
        if user_input in alphabet - used_letters:
            used_letters.add(user_input)
            if user_input in word_letters:
                word_letters.remove(user_input)
                print("Correct guess continue")
                # current word  
                word_list = [letter if letter in used_letters else '-' for letter in word]
                print("Current word: ", " ".join(word_list))
            else:
              print("Incorrect guess try again")
              lives -= 1
        elif user_input in used_letters:
           print("You have already guessed that letter. Try again.")
        
        
    if lives == 0:
        print("You died, sorry. The word was", word)
    else:
        print("Congratulations you have guessed the word correctly")

hangman()  # Call the hangman function to start the game