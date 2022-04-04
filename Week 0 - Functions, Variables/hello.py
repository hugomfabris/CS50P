#Ask user for their name
name = input("What's your name?")
#Remove whitespace from str and capitalize user's name
name = name.strip().title()
#Say hello to the user 
print("Hello, ", end="")
print(name)
print(f"Hello, {name}")

