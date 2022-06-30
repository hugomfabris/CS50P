import re

def main():
    print(convert(input("Hours: ")))

def convert(user_input):
    hours = re.search(r"(\d\d?)\s?:?\s?(\d?\d?)\s([ap])m\sto\s(\d\d?)\s?:?\s?(\d?\d?)\s([ap])m",  user_input, re.IGNORECASE)
    #The first else/if will ensure that the given input is in the correct format
    if hours:
        hours_list = list(hours.groups())
        if int(hours_list[0]) > 12 or int(hours_list[3]) > 12:
            raise ValueError
        else:
            n0 = int(hours_list[0])
            n2 = hours_list[2].lower()
            n3 = int(hours_list[3])
            n5 = hours_list[5].lower()
            #Here, after defining the capture groups as variables, we check if groups 1 and for are empty strings
            if hours_list[1] == '' and hours_list[4] == '':
                hours_list[1] = 0
                hours_list[4] = 0
                #On each condition we check if it's given AM or PM, making exception in the case it's 12
                if n2 == 'p' and n0 != 12:
                    n0 += 12
                    #After all checks, we use f string format to return the wanted result
                    return f'{n0:02}:00 to {n3:02}:00'
                elif n2 == 'a' and n0 == 12:
                    n0 -= 12
                    return f'{n0:02}:00 to {n3:02}:00'
                else:
                    if n5 == 'p' and n3 != 12:
                        n3 += 12
                        return f'{n0:02}:00 to {n3:02}:00'
                    elif n5 == 'a' and n3 == 12:
                        n3 -= 12
                        return f'{n0:02}:00 to {n3:02}:00'
                    else:
                        return f'{n0:02}:00 to {n3:02}:00'
            elif hours_list[1] == '' and hours_list[4] != '':
                n4 = int(hours_list[4])
                if int(hours_list[4]) >= 60:
                    raise ValueError
                else:
                    hours_list[1] = 0
                    if n2 == 'p' and n0 != 12:
                        n0 += 12
                        return f'{n0:02}:00 to {n3:02}:{n4:02}'
                    elif n2 == 'a' and n0 == 12:
                        n0 -= 12
                        return f'{n0:02}:00 to {n3:02}:{n4:02}'
                    else:
                        if n5 == 'p' and n3 != 12:
                            n3 += 12
                            return f'{n0:02}:00 to {n3:02}:{n4:02}'
                        elif n5 == 'a' and n3 == 12:
                            n3 -= 12
                            return f'{n0:02}:00 to {n3:02}:{n4:02}'
                        else:
                            return f'{n0:02}:00 to {n3:02}:{n4:02}'
            elif hours_list[1] != '' and hours_list[4] == '':
                n1 = int(hours_list[1])
                if int(hours_list[1]) >= 60:
                    raise ValueError
                else:
                    hours_list[4] = 0
                    if n2 == 'p' and n0 != 12:
                        n0 += 12
                        return f'{n0:02}:{n1:02} to {n3:02}:00'
                    elif n2 == 'a' and n0 == 12:
                        return f'{n0:02}:{n1:02} to {n3:02}:00'
                    else:
                        if n5 =='p' and n3 != 12:
                            n3 += 12
                            return f'{n0:02}:{n1:02} to {n3:02}:00'
                        elif n5 == 'a' and n3 == 12:
                            n3 -= 12
                            return f'{n0:02}:{n1:02} to {n3:02}:00'
                        else:
                            return f'{n0:02}:{n1:02} to {n3:02}:00'
            else:
                n1 = int(hours_list[1])
                n4 = int(hours_list[4])
                if int(hours_list[1]) >= 60 or int(hours_list[4]) >= 60:
                    raise ValueError
                else:
                    if n2 == 'p' and n0 != 12:
                        n0 += 12
                        return f'{n0:02}:{n1:02} to {n3:02}:{n4:02}'
                    elif n2 == 'a' and n0 == 12:
                        n0 -= 12
                        return f'{n0:02}:{n1:02} to {n3:02}:{n4:02}'
                    else:
                        if n5 =='p' and n3 != 12:
                            n3 += 12
                            return f'{n0:02}:{n1:02} to {n3:02}:{n4:02}'
                        elif n5 == 'a' and n3 == 12:
                            n3 -= 12
                            return f'{n0:02}:{n1:02} to {n3:02}:{n4:02}'
                        else:
                            return f'{n0:02}:{n1:02} to {n3:02}:{n4:02}'

    else:
        raise ValueError

if __name__ == "__main__":
    main()