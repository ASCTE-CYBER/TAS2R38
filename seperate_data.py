import csv
import re
from pathlib import Path
from pprint import pprint


class Dataset:
    name: str
    column_definitions = []
    rows = []

    def __init__(self, name):
        self.name = name

    def set_column_definitions(self, definitions):
        self.column_definitions = definitions

    def add_row(self, row):
        self.rows.append(row)
        print(self.rows)

    def export_to_csv(self):
        with open(f'data/{self.name}.csv', 'w') as f:
            f.write(''.join([f'{str(element)},' for element in self.column_definitions]).rstrip(',') + '\n')
            for row in self.rows:
                f.write(''.join([f'{str(element)},' for element in row]).rstrip(',') + '\n')


def load_data(file_path):
    data = []
    with open(file_path, 'r') as f:
        lines = f.readlines()
        for line in lines:
            line = line.replace('\n', '')
            print(line)
            if line.startswith('##') and line.endswith('header ##'):
                # print(line.split('##')[1].strip())
                dataset = Dataset(line.split('##')[1].strip())
                data.append(dataset)
            elif line.startswith('"{{'):
                data[-1].set_column_definitions(line.replace('{', '').replace('}', '').replace('"', '').split('\t'))
                # print(data[-1].column_definitions)
            elif line.startswith('#'):
                # print(f'nondata line "{line}" ignored')
                pass
            elif line.startswith('"'):
                # print(line.replace('"', '').split('\t'))
                data[-1].add_row(line.replace('"', '').split('\t'))
                print(data[-1].name)
                # print(data[-1].rows)

    return data


def main():
    data = load_data('./TAS2R38_dataset.txt')

    print(data[0].name)
    print(data[1].name)
    print(data[-1].name)

    for dataset in data:
        dataset.export_to_csv()
    pprint(data)


if __name__ == '__main__':
    main()
