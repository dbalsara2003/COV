import chardet
old_del = ','
new_del = ';'
new_f = []
rawdata = open(f"./data/sample_storefront_inventory.csv", 'rb').read()
result = chardet.detect(rawdata)
enc = result['encoding']
with open("./data/sample_storefront_inventory.csv", mode="r+", encoding=enc) as f:
    for line in f:
        new_f.append(str(line).replace(old_del, new_del))
with open("./data/sample_storefront_inventory.csv", mode="w+", encoding="utf-8") as f:
    f.writelines(new_f)
