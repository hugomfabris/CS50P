#Ask for user's input
userInput = input("Expression: ")
#Here we use the split string method to turn the user's input a list 
splitList = userInput.split(" ")
#Then we define our variables according to the values on the list 
x = float(splitList[0])
y = splitList[1]
z = float(splitList[2])
#Finally, we use conditional operators to check the value of y, our math operator, thereby returning the correct value 
if (y == '+'):
    print(x+z)
elif (y == '-'):
    print(x-z)
elif (y == '*'):
    print (x*z)
elif (y == '/'):
    print(x/z)