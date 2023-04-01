import csv

# Set the input and output file names
input_file = "./data/training.csv"
output_file = "./data/testing.csv"

# Open the input file and read in the data
with open(input_file, 'r') as f:
    reader = csv.DictReader(f)
    rows = list(reader)

# Set all floor_area_sf values to an empty string
for row in rows:
    row['floor_area_sf'] = ''

# Open the output file and write the modified data
with open(output_file, 'w', newline='') as f:
    writer = csv.DictWriter(f, fieldnames=reader.fieldnames)
    writer.writeheader()
    writer.writerows(rows)
