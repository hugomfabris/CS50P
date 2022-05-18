from textwrap import indent
import requests
import sys

#In this while loop, we'll analyse the commands gien by the user using sys library
while True:
    if len(sys.argv) == 1:
        sys.exit("Missing command-line argument")
    elif len(sys.argv) == 2:
        #This try/except block will catch the errors that can happen if the given arguemnt isn't a float and exit the programm, via sys.exit()
        try:
            amount = float(sys.argv[1])
            break
        except ValueError:
            sys.exit("Command-line argument is not a number")
    else:
        sys.exit("Too many command-line arguments")
#Here, this try/except block will ensure that a request exception is catched
try:
    obj = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json").json()
    price_scrapped = obj['bpi']['USD']['rate']
    price_list = []
    #Now we loop through the list, egt rid of the comma, so that we can turn the scrapped price into a float
    for char in price_scrapped:
        if char != ',':
            price_list.append(char)
        else:
            pass
    price = float(''.join(price_list))
    value = price * amount
    print(f"${value:,.4f}")
except requests.RequestException:
    print("A JSON error occurred")





