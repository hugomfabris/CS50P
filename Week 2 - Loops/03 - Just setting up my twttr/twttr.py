txt = input("Input: ").strip()
vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
new_txt = []

for i in txt:
    if i not in vowels:
        print(i, end="")


