import sys

#The outside if/else block will ensure that we have the correct number of arguments
if len(sys.argv) == 1:
    sys.exit("Too few command-line arguments")
elif len(sys.argv) > 2:
    sys.exit("Too many command-line arguments")
else:
    file = sys.argv[1]
    if not file.endswith(".py"):
        sys.exit("Not a Python file")
    #After checking if the passed argument has the .py extension, we'll use a try/except block to garantee that the file passed exist    
    else:
        try:
            with open(file, 'r') as file:
                count = 0
                #Finally, the make a loop through every line inside the file checking if it's not a comment neither whitespace
                for line in file:
                    if not line.lstrip().startswith("#") and not line.isspace():
                        count += 1
                print(count)
        except FileNotFoundError:
            sys.exit("File does not exist")
