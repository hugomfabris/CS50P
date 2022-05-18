import random

def main():
    level = get_level()
    i = 0
    score = 0
    while i < 10:
        temp_x = generate_integer(level)
        temp_y = generate_integer(level)
        j = 0
        while j < 3:
            try:
                question = int(input(f"{temp_x} + {temp_y} = "))
                answer = temp_x + temp_y
                if question == answer:
                    score += 1
                    j += 4
                else:
                    j += 1
                    print('EEE')
            except ValueError:
                print('EEE')
        if j == 3:
                
            print(f"{temp_x} + {temp_y} = {answer}")
        else:
            pass
        i += 1
    print(f"Score: {score}")

def get_level():
    while True:
        try:
            level = int(input("Level: "))
            if level == 1 or level == 2 or level == 3:
                return level
            else:
                pass
        except ValueError:
            pass

def generate_integer(level):
    if level == 1:
        integer = random.randrange(0, 9)
        return integer
    elif level == 2:
        integer = random.randrange(10, 99)
        return integer
    elif level == 3:
        integer = random.randrange(100, 999)
        return integer
    else:
        raise ValueError

if __name__ == "__main__":
    main()


