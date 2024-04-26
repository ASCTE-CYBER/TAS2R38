from pprint import pprint
import csv

def read_file():
    with open('temp/TAS2R38_dataset.txt') as f:
        data = f.read()
    return data

def build(data):
    lines = [l.strip() for l in data.splitlines() if len(l.split()) > 0]
    for line in lines:
        if line.startswith('#') and 'alter' in line.lower() and 'header' in line.lower():
            line = line[1:]










if __name__ == '__main__':
    data = read_file()
    build(data)
