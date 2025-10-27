# decision making with python

# making choises with code
# ctrl+/

# if
#   elif
#   else

# mood machine

# mood=input("how are you feeling today?")
# # i am asking user to tell how they are feeling
#
# if mood=="Happy"or mood=="happy" or mood=="hapy":
#     print("Yay you won a lottery isn't it?")
# elif mood=="Sad":
#     print("Awwwww sending you a hug")
# elif mood=="angry":
#     print("deep breath and lets count to ten")
# else:
#     print("interesting mood ! stay unique")


# second: Pizza party plan
# ask user how many friends are coming

# if fewer: than 3 , order a small pizza
# if between 3 and 6 order medium pizza
# if more than 6 order a big pizza

# friends=int (input("how many friends do you have?"))
# if friends <= 3:
#     print("you should order a small pizza")
# elif friends <= 4:
#     print("you should order a medium pizza")
# elif friends <= 6:
#     print("you should order a large pizza")
# else:
#     print("Go big")




# correct_password = "Education"
# for attemp in range (3):
#     password=input("enter your secret password")
#     if password == correct_password:
#         print("you are correct")
#     elif password=="education" or password=="educa tion" or password=="Education":
#         print("so close, check your spelling")
#     else :
#         print("sorry, try again")

#Exercise:  hogward sorting hat

trait=input("do you value bravery, intelligence, loyalty, ambition")
#bravery=griffindor
#intelligence=ravenclaw
#loyalty=hafflepuff
#ambition=slytherian
#else:("may be you are muggle")

if trait == "bravery":
    print("you are griffindor")
elif trait == "intelligence":
    print("you are ravenclaw")
elif trait == "loyalty":
    print("you are hafflepuff")
elif trait == "ambition":
    print("you are slytherian")

else:
    print("may be you are muggle")









