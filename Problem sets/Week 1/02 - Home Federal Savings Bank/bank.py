#Ask for some user's greeting
greeting = input("Greeting: ")
#Ignoring any leading whitespace in the user’s greeting, and treat the user’s greeting case-insensitively.
greeting = greeting.lstrip().lower()
#Finally checking with conditional statements
if (greeting.startswith("hello")):
    print("$0")
else:
    if greeting[0] == 'h':
        print("$20")
    else:
        print("$100")
