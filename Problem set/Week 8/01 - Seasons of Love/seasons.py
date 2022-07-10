from datetime import date
import inflect
import re
import sys

def main():
    user_input = input("Date of Birth: ")
    print(date_dealing(user_input))
#This function will use the regex seach method to check if the input given is in YYYY-DD-MM format
def check_birthday(birth_date):
    if re.search(r"\d{4}-\d{2}-\d{2}", birth_date):
        year, day, month = birth_date.split('-')
        return year, day, month
#Here, we deal with the formated date to output the total minutes in words format
def date_dealing(birth_date):
    p = inflect.engine()
    #With this try block we ensure that any None match object returned by check_birthday function will exit via sys.exit()
    try:
        year, day, month = check_birthday(birth_date)
    except:
        sys.exit('Invalid date')
    birth_date = date(int(year), int(day), int(month))
    today = date.today()
    #Here we use the date __sub__ method, that will return us a timedelta object
    delta = today - birth_date
    total_minutes = round(delta.total_seconds()/60)
    words = p.number_to_words(total_minutes)
    words = (words.replace(' and ', ' ')).capitalize() + ' minutes'
    return words

if __name__ == "__main__":
    main()
