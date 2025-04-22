import json
import csv
import os

# Reading and transforming a .txt file
def read_and_transform_txt(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        lines = file.readlines()
    # Example transformation: Strip whitespace and convert to uppercase
    transformed_lines = [line.strip().upper() for line in lines]
    return transformed_lines

# Reading and transforming a .json file
def read_and_transform_json(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        data = json.load(file)
    # Example transformation: Add a new key-value pair to each dictionary in a list
    if isinstance(data, list):
        for item in data:
            item['processed'] = True
    return data

# Reading and transforming a .csv file
def read_and_transform_csv(file_path):
    transformed_data = []
    with open(file_path, 'r', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        for row in reader:
            # Example transformation: Add a new column with a computed value
            row['new_column'] = int(row['existing_column']) * 2 if 'existing_column' in row else None
            transformed_data.append(row)
    return transformed_data

# Example usage
if __name__ == "__main__":

    
    print("Working directory:", os.getcwd())

    txt_result = read_and_transform_txt('project_py/example.txt')
    print("Transformed .txt:", txt_result)

    #json_result = read_and_transform_json('example.json')
    #print("Transformed .json:", json_result)

    #csv_result = read_and_transform_csv('example.csv')
    #print("Transformed .csv:", csv_result)

    