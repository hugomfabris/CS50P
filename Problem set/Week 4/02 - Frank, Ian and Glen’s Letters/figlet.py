import math
from pyfiglet import Figlet
from random import choice, random
import sys

figlet = Figlet()
fonts = figlet.getFonts()

#In the bigger loop, we'll analyse the arguments passed by the user
if len(sys.argv) == 1:
    user_input = input("Input: ")
    random_font = choice(fonts)
    figlet.setFont(font = random_font)
    print(f"Output: {figlet.renderText(user_input)}")
elif len(sys.argv) == 3:
    #In this inside loop we'll check if the arguments pass in our requisitions
    if sys.argv[1] == '-f' or sys.argv[1] == '--font':
        if sys.argv[2] in fonts:
            user_input = input("Input: ")
            choosen_font = fonts[fonts.index(sys.argv[2])]
            figlet.setFont(font = choosen_font)
            print(f"Output: \n {figlet.renderText(user_input)}")
        else:
            sys.exit('Invalid usage')
    else:
        sys.exit('Invalid usage')


else:
    sys.exit('Invalid usage')






