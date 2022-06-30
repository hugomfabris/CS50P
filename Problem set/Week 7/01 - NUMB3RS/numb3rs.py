import re

def main():
    print(validate(input("IPv4 Address: ")))


def validate(ip):
    match = re.search(r"^(2[0-4]\d|25[0-5]|1\d{2}|\d\d?)\.(2[0-4]\d|25[0-5]|1\d{2}|\d\d?)\.(2[0-4]\d|25[0-5]|1\d{2}|\d\d?)\.(2[0-4]\d|25[0-5]|1\d{2}|\d\d?)$", ip)
    try:
        return len(match.group()) != 4
    except AttributeError:
        return False
        
       

if __name__ == "__main__":
    main()


