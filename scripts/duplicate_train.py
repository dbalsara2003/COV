import csv

input_file = './data/converted_xlsx.csv'
output_file = './data/new_training4.csv'
n_times = 25


with open(output_file, 'w', newline='') as f_out:
    writer = csv.writer(f_out)
    with open(input_file, 'r') as f_in:
        reader = csv.reader(f_in)

        header = next(reader)
        writer.writerow(header)
        
        for row in reader:
            for i in range(n_times):
                writer.writerow(row)