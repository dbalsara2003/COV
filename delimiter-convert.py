import chardet

new_f = []
rawdata = open("./sample_storefront_inventory.csv", 'rb').read()
result = chardet.detect(rawdata)
enc = result['encoding']
with open("./sample_storefront_inventory.csv", mode="r+", encoding=enc) as f:
    for line in f:
        new_f.append(str(line).replace("\t", ","))
with open("./output.csv", mode="w+", encoding="utf-8") as f:
    f.writelines(new_f)
