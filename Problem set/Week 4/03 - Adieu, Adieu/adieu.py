import sys
def main():
    names = []
    while True:
        try:
            user_input = input("")
            names.append(user_input)
        except EOFError:
            if len(names) == 0:
                sys.exit()
            elif len(names) == 1:
                print(f"Adieu, adieu, to {names[0]}")
                break
            elif len(names) == 2:
                print(f"Adieu, adieu, to {names[0]} and {names[1]}")
                break
            else:
                print("Adieu, adieu, to", end='')
                for i in range(len(names) - 2):
                    print(" " + names[i] + ",", end='')
                print(" " + names[len(names) - 2] + ", and " + names[len(names) - 1])
                break
main()