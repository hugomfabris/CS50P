def main():
    user_input = input('').strip()
    print(shorten(user_input))


def shorten(word):
    word = str(word)
    vowels = ['a', 'e', 'i', 'o', 'u']
    shorten_word = ''
    for char in word:
        if char.lower() not in vowels:
            shorten_word += char
    return shorten_word

if __name__ == "__main__":
    main()



