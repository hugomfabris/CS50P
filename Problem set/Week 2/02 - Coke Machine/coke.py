#First we set the due value to 50 and print it
due = 50
print(f"Amount due: {due}")
#Now we use a while loop to make a message with the due value appear until it's not zero
while due > 0:
    coin = int(input("Insert coin: "))
    if coin != 25 and coin != 10 and coin != 5:
        print(f"Amount due: {due}")
    else:
        if due > coin:
            due -= coin
            print(f"Amount due: {due}")
        elif coin == due:
            print("Change owed: 0")
            break
        else:
            due -= coin
            due = abs(due)
            print(f"Change owed: {due}")
            break



