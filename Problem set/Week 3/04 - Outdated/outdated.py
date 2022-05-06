months = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
]
#Here we make a while loop with a try/except block to prompt the user again in case of incorrect input or ValueErrors
while True:
    try:
        user_input = input("Date: ")
        date = user_input.split(' ')
        #We check first the cases that we receive our date in Month day, year format
        if len(date) > 1:
            x, y, z = date
            #Here we get rid of the comma after day, turn it into and integer and check if it has 1 or 2 digits
            if len(y) == 2:
                y = int(y[0]) 
            elif len(y) == 3:
                y = int(y[0:2]) 
            else:
                pass
            #Now we check if day and month are valid, print the result and break the loop
            if x in months and y > 0 and y <= 31:
                month_index = months.index(x) + 1
                if month_index < 10 and y < 10:
                    print(f"{z}-0{month_index}-0{y}")
                    break
                elif month_index < 10 and y >= 10:
                    print(f"{z}-0{month_index}-{y}") 
                    break
                elif month_index >= 10 and y < 10:
                    print(f"{z}-{month_index}-0{y}") 
                    break
                else:
                    print(f"{z}-{month_index}-{y}") 
                    break 
            #When any of the conditions are not satisfied, we'll repront the user with else: pass 
            else:
                pass
        #We check the cases that we receive our date in mm/dd/year format 
        else:
            a, b, c = user_input.split('/')
            a = int(a)
            b = int(b)
            c = int(c)
            #Now we check if day and month are valid, print the result and break the loop
            if a > 0 and a <= 12 and b > 0 and b <= 31:
                if a < 10 and b < 10:
                    print(f"{c}-0{a}-0{b}")
                    break
                elif a >= 10 and b < 10:
                    print(f"{c}-{a}-0{b}")
                    break
                elif a < 10 and b >= 10:
                    print(f"{c}-0{a}-{b}")
                    break
                else:
                    print(f"{c}-{a}-{b}")

                
            
    except ValueError:
        pass 
