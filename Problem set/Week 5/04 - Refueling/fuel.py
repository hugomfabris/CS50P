def main():
    fraction = input("Fraction: ")
    converted = convert(fraction)
    gauged = gauge(converted)
    print(gauged)


def convert(fraction):
    z = 0
    while True:
        div_index = fraction.index("/")
        x = int(fraction[0:div_index])
        y = int(fraction[div_index + 1:])
        z = round(x/y * 100)
        if z > 100:
            raise ValueError("X can't be greater than Y")
        elif y == 0:
            raise ZeroDivisionError("Y can't be zero")
        else:
            return z

def gauge(percentage):
    if percentage >= 99:
        return 'F'
    elif percentage <= 1:
        return 'E'
    else:
        return f"{percentage}%"





  
if __name__ == "__main__":
    main()


