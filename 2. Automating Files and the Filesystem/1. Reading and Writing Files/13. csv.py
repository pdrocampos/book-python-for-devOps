import csv

file_path = '/Users/kbehrman/Downloads/registered_user_count_ytd.csv'
with open(file_path, newline='') as csv_file:
    off_reader = csv.reader(csv_file, delimiter=',')
    for _ in range(5):
        print(next(off_reader))









