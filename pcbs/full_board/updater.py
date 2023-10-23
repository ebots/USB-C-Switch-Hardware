import csv

updates = {
    "C8734": -90,
    "C20917": 180,
    "C73088": 180,
    "C5446": 180,
    "C783420": -90,
    "C500787": -90,
    "C15127": 180,
}

part_type = {}
with open('production/bom.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    for row in csv_reader:
        if line_count == 0:
            line_count = 1
            continue
        print(row)
        for key in row[0].split(", "):
            part_type[key] = row[-1]
print(part_type)
with open('production/positions.csv') as csv_file:
    with open('production/positions_new.csv', mode='w') as csv_file_out:
        csv_reader = csv.reader(csv_file, delimiter=',')
        csv_writer = csv.writer(csv_file_out, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        line_count = 0
        for row in csv_reader:
            if line_count == 0:
                line_count = 1
                csv_writer.writerow(row)
                continue

            print(row)
            if row[0] in part_type:
                this_part = part_type[row[0]]
                print (this_part)
                if this_part in updates:
                    row[-2] = str(float(row[-2])+updates[this_part])
                    print (row)
            csv_writer.writerow(row)

    
