# c=22/7
# print(c)
# round(c)

# user defined function

# def say_hello():   #defining a function
#     print("Hello World!")
# say_hello()   #calling a function
# say_hello()
# say_hello()
# say_hello()


# def greet(name): #function with parameters
#     print("Welcome", name, "to the adventure!")
# greet("Paolo")
# def greet(color):
#     print("My favorite color is", color)
# greet("blue")

# def start_game():
#     print("Game starting")
# def find_tresure():
#     print("Tresure found")
# def play():
#     print("Playing")
#     find_tresure()
#     find_tresure()
#     print("Game over")
# play()


# Modules

# import math
# math.pi
# print(math.sqrt(16))
# math.floor(789.99)



# We wish to create a program to play a game of "Guess the Number".
#
# Start by creating a new python file called module_tasks.py and store it in the week4 folder
#
# The program should use the module random.

import random as rnd
def play_guess_the_number():
# The program should start by displaying the message "Please enter the minimum value:"
    print("please enter the minumum value")

# The program should then read in the user's number.

    min_value=int(input("please enter the minumum value"))




# The program should then display the message "Please enter the maximum value:"
    print("please enter the maximum value")

# The program should then read in the user's number.
max_value=int(input("please enter the minumum value"))

guess_number=rnd.randint(min_value, max_value)
    print(f"you have guessed the number is {min_value} and it was {max_value}.")


# The program should then generate and store a random number between the minimum and maximum value specified by the user.
# The program should then display the message "I am thinking of a number between {min} and {max}.  Can you guess what it is?" where {min} and {max}are the minimum and maximum values specified by the user.
# The program should then do the following repeatedly until the user guesses the correct answer:
#     read in the user's guess
#     if the guess is too low then display the message "Your guess is too low."
#     otherwise if the guess is too high then display the message "Your guess is too high."
#     In any case, display the message "Try again:".
# The program should display the following message once the user guessed the correct number: "Congratulations! You guessed my number!".
#
# Once you have the above program working as intended, you should turn it into a user-defined function name play_guess_the_number and call the function appropriately.
#
#
# An example run of such a program is shown below:
#
# Please enter the minimum value:
# 1
# Please enter the maximum value:
# 10
# I am thinking of a number between 1 and 10. Can you guess what it is?
# 2
# Your guess is too low.
# Try again:
# 9
# Your guess is too high.
# Try again:
# 5
# Congratulations! You guessed my number!
















