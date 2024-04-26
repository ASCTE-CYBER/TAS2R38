import csv
import sys
from pprint import pprint

def get_filename():
    if len(sys.argv) != 2:
        print('Usage: python build_dataset.py <output_filename>')
        sys.exit(1)
    return sys.argv[1]

def build(output_filename):
    with open('data/temp.txt', newline='') as f:
        data = f.read()

    lines = []
    for item in data.splitlines():
        if not len(item.split()) > 0:
            continue
        item = item.strip()
        #item = item.replace('"', '')
        item = item.replace('}', '')
        item = item.replace('{', '')
        item = item.split()
        lines.append(item)

    with open(f'data/{output_filename}.csv', 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerows(lines)

if __name__ == '__main__':
    output_filename = get_filename()
    build(output_filename)
    print(f'File {output_filename}.csv created successfully')
