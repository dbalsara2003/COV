##I don't really know how we want the data to be parsed so if someone could work on this with me would be very helpful :P

import json
def csvParse(file):
    print('oogabooga :)')
    pass

def remove_duplicate_rows(file):
    new_lines = []
    with open(file, mode='r') as f:
        lines = f.readlines()
        for line in lines:
            if not line in new_lines:
                new_lines.append(line)

    print(new_lines)

    with open(f"{file}", mode='w') as f:
        f.writelines(new_lines)

def add_id(polypoint, output):
    new_lines = []
    with open(polypoint, mode='r') as f:
        lines = f.readlines()
        for line in lines:
            new_lines.append(line.replace('\n','').split(';'))

    ids = []

    with open('./data/storefronts_opendata.csv', mode='r') as f:
        for line in f.readlines():
            ids.append([line.split(';')[0], line.split(';')[8]])
    
    # example array[1] = "{""coordinates"": [-123.14981916780552, 49.27268602461876], ""type"": ""Point""}"
    for index, array in enumerate(ids):
        #print("Index: ", index, "Array: ", array)
        if index == 0:
            continue
        array[1] = array[1].replace('""', '"')[1:-1]
        array[1] = str(tuple(json.loads(array[1])['coordinates']))
        ids[index] = array
    final_lines = []
    with open(output, mode='a+') as f:
        for count, line in enumerate(new_lines):
            if count == 0:
                line.append('id')
                continue
            collected = []
            for row in ids:
                if line[0] == row[1]:
                    collected.append(row[0])
            line.append(collected)
        for line in new_lines:
            row_str = ""
            for bit in line:
                row_str += ';' + str(bit)
            f.write(row_str[1:] + '\n')

def make_storefronts_with_polys(input, output):
    lines = []
    with open(input, mode='r') as f:
        tlines = f.readlines()
        for line in tlines:
            lines.append(line.replace('\n','').split(';'))

    final_lines = []
    with open('./data/storefronts_opendata.csv', mode='r') as f:
        for count, line in enumerate(f.readlines()):
            line_data = line.replace('\n','').split(';')
            if count == 0:
                line_data.append('polygon')
                final_lines.append(line_data)
                continue
            for other_line in lines:
                #print(line_data[0], other_line[2])
                if str(line_data[0]) in other_line[2]:
                    line_data.append(other_line[1])
                    final_lines.append(line_data)
                    break
            if len(line_data) < 11:
                line_data.append("N/A")
            if not line_data in final_lines:
                final_lines.append(line_data)
    print(len(final_lines))
    with open(output, mode='w') as f:
        for line in final_lines:
            print(line)
            row_str = ""
            for bit in line:
                row_str += ';' + str(bit)
            f.write(row_str[1:] + '\n')
    return final_lines
        