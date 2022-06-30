from validator_collection import validators, errors

def main():
    print(validate(input("E-mail: ")))

def validate(email_address):
    try:
        if validators.email(email_address):
            return "Valid"
    except errors.InvalidEmailError:
        return 'Invalid'
    except errors.EmptyValueError:
        return 'Invalid'

if __name__ == "__main__":
    main()  

