import sys
import csv

#First we check the user arguments given
if len(sys.argv) < 3:
    sys.exit("Too few command-line arguments")
elif len(sys.argv) > 3:
    sys.exit("Too many arguments")
else:
    #Here we use the try/except block to make sure the file given by the user exist
    try:
        input_file = sys.argv[1]
        output_file = sys.argv[2]
        #Openning the file, we'll split the name into first and last as required with a for loop and append that as a list of dictionaries
        with open(input_file, newline='') as file:
            students = []
            reader = csv.DictReader(file)
            for row in reader:
                last_name, first_name = row['name'].split(',')
                first_name = first_name.strip()
                students.append({
                    'first': first_name,
                    'last': last_name,
                    'house': row['house']
                })
    except FileNotFoundError:
        sys.exit(f"Could not read {input_file}")
    #Finally, we'll name the output as the second argument provided by the user and write the students list into it
    with open(output_file, 'w', newline='') as file:
            writer = csv.DictWriter(file, fieldnames=['first', 'last', 'house'])
            writer.writeheader()
            for row in students:
                writer.writerow({'first': row['first'], 'last': row['last'], 'house': row['house']})



