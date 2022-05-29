def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print(True)
    else:
        print(False)


def is_valid(s):
    s = s.strip().upper()
    s2 = s[0:2]
    s_end = s[2:]
    if len(s) >= 2 and len(s) <= 6:
        if s2.isalpha():
            if len(s_end) == 0:
                return True
            elif len(s_end) == 1 and s_end[0] != '0':
                return s_end.isalpha() or s_end.isnumeric()
            elif len(s_end) == 2 and s_end[0] != '0':
                return s_end[0].isalpha() or s_end.isnumeric()
            elif len(s_end) == 3 and s_end[0] != '0':
                return s_end.isalpha() or s_end[0:2].isalpha() or s_end[0].isalpha() or s_end.isnumeric()
            elif len(s_end) == 4 and s_end[0] != '0':
                return s_end.isalpha() or s_end[0:3].isalpha() or s_end[0:2].isalpha() or s_end[0].isalpha() or s_end.isnumeric()
            else:
                return False
        else:
            return False
    else:
        return False

if __name__ == "__main__":
    main()
