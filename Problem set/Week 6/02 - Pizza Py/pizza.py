import sys
import tabulate
import csv

if len(sys.argv) == 1:
    sys.exit("Too few command-line arguments")
elif len(sys.argv) > 2:
    sys.exit("Too many arguments")
else:
    file = sys.argv[1]
    try:
        if file.endswith(".csv"):
            catalogue = []
            with open(file) as file:
                reader = csv.reader(file)
                for row in reader:
                    catalogue.append({
                        'pizza': row[0],
                        'small': row[1],
                        'large': row[2]
                    })
                print(tabulate.tabulate(catalogue, headers="firstrow", tablefmt="grid"))
        else:
            sys.exit("Not a CVS file")
    except FileNotFoundError:
        sys.exit("File does not exist")