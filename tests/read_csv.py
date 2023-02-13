import csv

def read_csv_data(filename):
    rows = []
    csv_data = open(str(filename), "r")
    content = csv.reader(csv_data)

    # skip header line
    next(content, None)

    # add rows to list
    for row in content:
        rows.append(row)
        #print(row)

    print(rows)
    return rows
