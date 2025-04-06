import random
def guess_number(x):
    random_number = random.randint(1,x)
    guess =0
    while guess != random_number:
        guess=int(input(f"Guess a nubmer between 1 and {x}: "))
        if guess <random_number:
            print("sorry the number is too low try  again")
        elif guess > random_number:
            print("sorry the number is too high try again")
        else:
            print(f"congratulations you have guessed the number {random_number} correctly")
guess_number(10)