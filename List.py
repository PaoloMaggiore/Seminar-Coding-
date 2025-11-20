# 🐍 Python Lists & Tuples — Interactive Lab (2-Hour Session)

# Welcome to this hands-on lab for **Python lists and tuples**.

# This session includes:

# - Guided explanations
# - Practice exercises
# - Interactive widgets
# - Mini-project
# - Quizzes
# - Challenges

# Run each code cell using **Shift + Enter**.
## 2️⃣ Python Lists — Basics

# A **list** is:

# - ordered
# - mutable (can change)
# - written with **[ ]**
# - can store mixed types

# # Example:
# numbers = [10, 20, 30, 40]
# fruits = ["apple", "banana", "orange"]
# names = ["Alice", "Bob", "Charlie"]
# print(numbers)
# print(names)
# print(numbers, names, fruits)
#
# ### ✏️ Exercise 1 — Create Your Own List

# Tasks:

# 1. Create list `fruits` with 4 fruits
# 2. Print first and last
# 3. Change one element
# 4. Print updated list
# fruits = ["apple", "banana", "orange", "mango"]
# print(fruits [0], fruits [3])
# print(fruits[1])
# fruits.append("cherry")
# print(fruits)
# print(len(fruits))
#
#
# ###  Exercise 2 — Index & Slice
#
# # Given:
#
# # ```python
# nums = [5, 10, 15, 20, 25, 30]
# print(nums[1])
#
# # Print 2nd element
#
# # Print last using negative index
# print(nums[-5])
#
#
# # Print slice [10, 15, 20]
# x=slice(1,3)
# print(nums[x])
#
#
# # Print every second element
#
#
# # Exercise 3
#
# scores = [88,92,75,94,81]
#
# # append new score
# scores.append(99)
# print(scores)
#
# # remove a score
#
# scores.pop(1)
# print(scores)
#
# # sort
# scores.sort()
# print(scores)
#
# # print highest & lowest
#
# scores.reverse()
# print(scores)



# Shopping List Program

# Create an empty list called shopping.
shopping = []


# Ask the user (or pretend to ask) to:
# Add at least 3 items
shopping.append("cheese")
shopping.append("pizza")
shopping.append("shampoo")
shopping.append("meat")
print(shopping)



# Remove 1 item
shopping.remove("cheese")
shopping.remove("pizza")
print(shopping)

# Print the final list
print(shopping)







