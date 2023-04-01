import csv

# Set the input and output file names
input_file = "./data/output.csv"
output_file = "./data/reformatted_output.csv"

# Open the input file and read in the data
with open(input_file, 'r') as f:
    reader = csv.reader(f, delimiter=',')
    rows = list(reader)

# Open the output file and write the reformatted data
with open(output_file, 'w', newline='') as f:
    writer = csv.writer(f)
    for row in rows:
        # Join the row elements into a single string with spaces as the separator
        # joined_row = " ".join(row)
        # # Split the joined row into separate fields
        # fields = joined_row.split()
        # Write the fields to the output file as a new row
        writer.writerow(row)