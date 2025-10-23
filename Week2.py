print("welcome to week2")

name = input("enter your name")
print(f"hello {name}")

a = 5
b = 10
print(f"the sum of {a} and {b} is {a + b}")

text= input("enter your text:").strip()
width=len(text) +4
print("*"*width)
print(f"*{text}*")
print("*"*width)

title = "System Unit"
dash = "_" * len(title)
print(title)
print(dash)

phrase = "python is awesome"
print(phrase.upper())
print(phrase.capitalize())

name = "Valentine"
age = 20
height = 5.9

print ("name:", name)
print("age:" , age)

print (f" my name is {name} and I am {age} years old.")

name = input("what your name?")
print(f"your name is {name} and I am {age} years old.")
print(f"next year you will be {age + 1} years old.")

lives = int(input("please enter the number for lives: "))
energy = int(input("please enter the number for energy: "))
stemina = int(input("please enter the number for stemina: "))

print("\nhealth has been set")
print("lives:  ", " & " * lives)
print("energy: ", " % " * energy)
print("stemina:", " * " * stemina)

num = int(input("please enter your number: "))
if num > 0:
    print("positive number")
elif num < 0:
    print("negative number")


marks = int(input("please enter your marks"))
if marks >= 80:
    print("grade: A")

elif marks >= 60:
    print("grade: B")
elif marks >= 40:
    print("grade: C")
else:
    print("fail")














