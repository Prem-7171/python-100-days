try:
    age = int(input("How old are you?"))
except ValueError:
    print("Type and integer such as 15")
    age = int(input("How old are you?"))
if age > 18:
    print(f"You can drive at age {age}.")
