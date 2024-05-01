# import csv
# import re
# from pathlib import Path
# from pprint import pprint


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

    # Custom export to CSV
    def export_to_csv(self):
        with open(f'data/{self.name}.csv', 'w') as f:
            f.write(''.join([f'{str(element)},' for element in self.column_definitions]).rstrip(','))
            for row in self.rows:
                f.write('\n' + ''.join([f'{str(element)},' for element in row]).rstrip(','))


def load_data(file_path):
    data: Dataset = None
    with open(file_path, 'r') as f:
        lines = f.readlines()
        for line in lines:
            line = line.replace('\n', '')
            if line.startswith('##') and line.endswith('header ##'):
                if data is not None:
                    data.export_to_csv()
                    print(f'exported {data.name}')

                data = Dataset(line.split('##')[1].strip())
                data.rows = []
                data.column_definitions = []
            elif line.startswith('"{{'):
                data.set_column_definitions(line.replace('{', '').replace('}', '').replace('"', '').split('\t'))
                # print(data[-1].column_definitions)
            elif line.startswith('#'):
                print(f'nondata line "{line}" ignored')
            elif line.startswith('"'):
                # print(line.replace('"', '').split('\t'))
                data.add_row(line.replace('"', '').split('\t'))
                # print(data.name)


def main():
    load_data('./TAS2R38_dataset.txt')


if __name__ == '__main__':
    main()
