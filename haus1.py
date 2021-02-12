import csv

def csv.reader(file_obj):
    reader = csv.reader(file_obj)
    for row in reader:
        a = row[0]
        b = row[3]
        c = a,b
        d = a,b.replace(" ","-")
        print(d)
        return reader
    # for new in row:

if __name__ == "__main__":
    csv_path = 'mls.csv'
    with open(csv_path, 'r') as f_obj:
        # csv_reader(f_obj)

def csv_writer(obj,file):
    with open(file, 'w') as new_file:
        writer = csv.writer(new_file, delimiters)
