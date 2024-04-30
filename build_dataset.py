import csv
import re
from pathlib import Path
from pprint import pprint

def load_data(file_path):
    data = []
    with open(file_path, 'r') as f:
        reader = csv.DictReader(f)
        for row in reader:
            data.append(row)
    return data

def parse(string):
    data = []
    for line in string.splitlines():
        if line.startswith('## ') and line.endswith('header ##'):
            block = line

def main():
    data = load_data()
    pprint(data)

if __name__ == '__main__':
    main()
