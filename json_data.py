import csv
import json
import os

csv_file = 'new_data.csv'
json_file = 'new_data.json'

if os.path.exists(csv_file):
    with open(csv_file, 'r') as csvfile:
        csv_reader = csv.DictReader(csvfile)
        num_rows = sum(1 for row in csv_reader)
        print("Number of rows in CSV file:", num_rows)
        csvfile.seek(0)
        data = [row for row in csv_reader]

    print("Number of rows read:", len(data))
    json_data = json.dumps(data)

    with open(json_file, 'w') as jsonfile:
        jsonfile.write(json_data)

    print("JSON data written to", json_file)
else:
    print("Error: CSV file not found -", csv_file)
