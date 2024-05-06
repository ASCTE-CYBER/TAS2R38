from pathlib import Path
import csv
from pprint import pprint

def load_data(csv_file):
    data = []
    data_folder = Path('./data').resolve()
    csv_file = data_folder / csv_file
    with open(csv_file) as f:
        reader = csv.DictReader(f)
        for row in reader:
            data.append(row)
    return data

def build_individual_to_disease_map(individual_data, individual_to_disease_data):
    data = []
    individual_ref = [i['individualid'] for i in individual_to_disease_data]
    for individual in individual_data:
        if individual['id'] not in individual_ref:
            continue
        record = {
            'id': individual['id'],
            'panel_size': individual['panel_size'],
            'disease_id': None
        }
        for r in individual_to_disease_data:
            if r['individualid'] == individual['id']:
                disease_id = r['diseaseid']
                if disease_id == '00000':
                    disease_id_key = 0
                elif disease_id == '00198':
                    disease_id_key = 1
                elif disease_id == '01502':
                    disease_id_key = 2
                else:
                    disease_id_key = 99
                record['disease_id'] = disease_id_key
                break
        data.append(record)
    return data

def write_data(data):
    data_folder = Path('./data').resolve()
    csv_file = data_folder / 'individuals_to_diseases_mapped.csv'
    with open(csv_file, 'w', newline='') as f:
        fieldnames = ['id', 'panel_size', 'disease_id']
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        for row in data:
            writer.writerow(row)

def main():
    individual_data = load_data('Individuals.csv')
    individual_to_disease_data = load_data('Individuals_To_Diseases.csv')
    individual_to_disease_map = build_individual_to_disease_map(individual_data, individual_to_disease_data)
    print('Writing data')
    write_data(individual_to_disease_map)

if __name__ == '__main__':
    main()
