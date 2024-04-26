from pprint import pprint
import csv
from pathlib import Path

path = Path('data').resolve()
files = [f for f in path.iterdir() if f.is_file() and f.suffix == '.csv']

for file in files:
    with open(file) as f:
        reader = csv.reader(f)
        rows = [line for line in reader]
    header, data = rows[0], rows[1:]
    header_length = len(header)
    for row in data:
        if len(row) != header_length:
            print(f'{file.name} --> Row {data.index(row)} has {len(row)} columns, expected {header_length}')



    break

