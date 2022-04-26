#First we define a function to take user’s input formatted in 24-hour time as #:## or ##:##
def main():
    userTime = input("What time is it? ")
    if (convert(userTime) >= 7 and convert(userTime) <= 8.0):
        print("breakfast time")
    elif (convert(userTime) >= 12 and convert(userTime) <= 13.0):
        print("lunch time")
    elif (convert(userTime) >= 18 and convert(userTime) <= 19.0):
        print("dinner time")

#Here we define the function that we'll be using inside of main to convert the user's input format into float, thereby helping us to buid the main function logic
def convert(time):
    hours, minutes = time.split(":")
    hours = float(hours)
    minutes = float(minutes)
    return hours + (minutes/60)

main()