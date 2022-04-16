def main():
    userTime = input("What time is it? ")
    if (convert(userTime) >= 7 and convert(userTime) <= 8.0):
        print("breakfast time")
    elif (convert(userTime) >= 12 and convert(userTime) <= 13.0):
        print("lunch time")
    elif (convert(userTime) >= 18 and convert(userTime) <= 19.0):
        print("dinner time")


def convert(time):
    hours, minutes = time.split(":")
    hours = float(hours)
    minutes = float(minutes)
    return hours + (minutes/60)

main()