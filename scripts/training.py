import csv

# Set the input and output file names
input_file = "./data/converted_xlsx.csv"
output_file = "./data/training2.csv"

# Open the input file and read in the data
with open(input_file, 'r') as f:
    reader = csv.DictReader(f)
    rows = list(reader)

# Filter the rows based on whether the floor_area_sf column has a value
filtered_rows = [row for row in rows if row['floor_area_sf']]

# Open the output file and write the filtered rows
with open(output_file, 'w', newline='') as f:
    writer = csv.DictWriter(f, fieldnames=reader.fieldnames)
    writer.writeheader()
    writer.writerows(filtered_rows)
