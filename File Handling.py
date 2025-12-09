# example1 = "testo.txt"
# with open(example1, "r") as f:
#     content1 = f.read()
#     print(content1)
#     f.close()
#     print("file closed:", f.closed)


import csv

with open("ETX sheet.csv") as file:
  csv_reader = csv.reader(file)
  headings = next(csv_reader)
  print(headings)






