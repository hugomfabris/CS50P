import re

def main():
    print(count(input("Text: ")))

def count(s):
    count_list = re.findall(r"\bum\b", s, re.IGNORECASE)
    return len(count_list)


if __name__ == "__main__":
    main()