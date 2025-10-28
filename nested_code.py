# cover = input("What type of cover does the book have (soft or hard)? ").strip().lower()
# perfect = input("Is the book perfect bound (yes or no)? ").strip().lower()
#
# if cover == "soft":
#     message = "Soft cover books are easy to carry."
# elif cover == "hard":
#     message = "Hard cover books are durable and long-lasting."
# else:
#     message = "No recognized cover type — maybe your book is an ebook!"
#
# if perfect == "yes":
#     if cover == "soft":
#         message += " Soft cover perfect bound books are very popular!"
#     else:
#         message += " It is perfectly bound by the maker."
#
# print(message)
#


location = input("where should I look").strip().lower()
if location == "in the bedroom":
    look = input("where in the bedroom should I look").strip().lower()
    if look == "in the cupboard":
        print("found some mess but no phone")
    else:
        print("found some mess but no phone in the cupboard, I am still looking")
elif location == "in the bathroom":
    look = input("where in the bathroom should I look").strip().lower()
    if look == "in the bathtub":
        print("found a rubber duck but no phone")
    else:
        print("found some shampoo and soap but not phone")
elif location == "in the living room":
    look = input("where in the living room should I look").strip().lower()
    if look == "on the table":
        print("yes, he/she found the phone")
    else:
        print("Congrats, you need a new phone")
else:
    print("I don't know where to keep the rubber duck")
