grocery_list = { }

while True:
    try:
        item = input().strip().upper()
        if item in grocery_list:
            grocery_list[item] += 1
        else:
            grocery_list[item] = 1
    except EOFError:
        sorted_list = sorted(list(grocery_list))
        for item in sorted_list:
            print(f"{grocery_list[item]} {item}")
        break
    except KeyError:
        pass
    








