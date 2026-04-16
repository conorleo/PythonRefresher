import csv


# Read from CSV as a list
with open("input.csv") as csv_file:
    reader = csv.reader(csv_file, delimiter=',') # csv.reader() returns an iterable reader object, delimiter specifies the character that separates the values in the csv file
    header_row = next(reader) # skip (and assign) the header row
    print(f"Column names: {header_row}")
    for row in reader: # iterate through the remaining rows in the csv file
        print(f"{row[0]} is in the {row[1]} faculty and {row[2]} department.") # row is a list of strings, index starts at 0

# Read from CSV as a dict
with open("input.csv") as csv_file:
    reader = csv.DictReader(csv_file, delimiter=',', fieldnames=['name', 'faculty', 'department']) # keys are given by the optional fieldnames parameter (or inferred from the first row of the csv file if not provided)
    for row in reader:
        print(f"{row['name']} is in the {row['faculty']} faculty and {row['department']} department.")


# Write to CSV from a list
header = ['name', 'faculty', 'department']
rows = [
    ['Alice Smith', 'Science', 'Chemistry'],
    ['Ben Williams', 'Eng', 'EEE'],
    ['Bob Jones', 'Science', 'Physics'],
    ['Andrew Taylor', 'Eng', 'Computing']
]
with open("output.csv", 'w') as csv_file:
    writer = csv.writer(csv_file, delimiter=',')
    writer.writerow(header) # write a single line
    writer.writerows(rows)  # write multiple lines

# Write to CSV from a dict
rows = [
    {'name': 'Alice Smith', 'faculty': 'Science', 'department': 'Chemistry'},
    {'name': 'Ben Williams', 'faculty': 'Eng', 'department': 'EEE'},
    {'name': 'Bob Jones', 'faculty': 'Science', 'department': 'Physics'},
    {'name': 'Andrew Taylor', 'faculty': 'Eng', 'department': 'Computing'}
]
with open("output.csv", 'w') as csv_file:
    writer = csv.DictWriter(csv_file, fieldnames=header, delimiter=',') # specify header list
    writer.writeheader() # write the header row
    for row in rows:
        writer.writerows(rows) # write a single line from a dict
