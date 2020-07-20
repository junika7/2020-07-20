letter = input("Enter: ")

if letter.isalpha():
    print(f"{letter} is alphabet.")
elif letter.isnumeric():
    print(f"{letter} is number.")
else:
    print("?")
