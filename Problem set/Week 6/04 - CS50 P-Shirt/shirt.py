import sys
from PIL import Image, ImageOps

user_input = sys.argv[1].lower()
user_output = sys.argv[2].lower()

#This function will deal with the user command-line arguments
def command_checker():
    if len(sys.argv) < 3:
        sys.exit("Too few command-line arguments")
    elif len(sys.argv) > 3:
        sys.exit("To many command-line arguments")
    else:
        #Here we ensure that input and output are in the correct format and have the same extensions
        if user_input.endswith('.png') or user_input.endswith('.jpeg') or user_input.endswith('.jpg'):
            if user_output.endswith('.png') or user_output.endswith('.jpeg') or user_output.endswith('jpg'):
                if user_input[len(user_input) - 4:] != user_output[len(user_output) - 4:]:
                    sys.exit("Input and output have different extensions")
            else:
                sys.exit("Invalid output")
        else:
            sys.exit("Invalid input")

def main():
    command_checker()
    try:
        background_img = Image.open(user_input)
    except FileNotFoundError:
        sys.exit("File not found")
    #Here we use the methods of the PIL library
    shirt_file = Image.open("shirt.png")
    size = shirt_file.size
    muppet = ImageOps.fit(background_img, size)
    muppet.paste(shirt_file, shirt_file)
    muppet.save(user_output)

if __name__ == "__main__":
    main()





