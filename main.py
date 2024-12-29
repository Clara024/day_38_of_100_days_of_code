mystring = input("Introduce yourself: ")
for letter in mystring:
  if letter.lower() == "g":
    print("\033[34m", end="")
  elif letter.lower() == "c":
    print("\033[32m", end="")
  elif letter.lower() == "i":
    print('\033[35m', end="")
  elif letter.lower() == "a":
    print('\033[33m', end="")
  elif letter.lower() == "e":
    print('\033[31m', end="")
  elif letter.lower() == " ":
    print('\033[0m', end="")
  print(letter,end="")