def main():
    print(fuel_gauge())

def fuel_gauge():
    #Here we use a while loop in order not to let the program finish without a proper output
    while True:
#Inside the try block we'll find the index of the division operator, convert and define x and y as the integers before and after it and z as our rounded result
        try:
            user_input = input("Fraction: ")
            div_index = user_input.index("/")
            x = int(user_input[0:div_index])
            y = int(user_input[div_index + 1:])
            z = round(x/y * 100)
#We'll use except to handle possible errors
        except(ValueError, ZeroDivisionError):
            pass
#If everything works, we can check for final conditions
        else:
            if z > 100:
                pass
            elif z >= 99:
                return 'F'
            elif z <= 1:
                return 'E'
            else:
                return f"{z}%"
main()