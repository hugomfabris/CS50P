def main():
    greeting = input("Greeting: ")
    print(value(greeting))


def value(greeting):
    greeting = greeting.lstrip().lower()
    if (greeting.startswith("hello")):
        return 0
    else:
        if greeting[0] == 'h':
            return 20
        else:
            return 100


if __name__ == "__main__":
    main()


