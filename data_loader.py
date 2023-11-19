import csv

loaded_data = dict()

class Table:
    def __init__(self, schema, entries):
        self._schema = schema
        self._entries = entries

    def schema(self):
        return self._schema

    def entries(self):
        return self._entries
    
def get(file_name):
    if file_name in loaded_data:
        return 
    
    rows = []

    with open(file_name, 'r') as file:
        csvreader = csv.reader(file)
        schema = next(csvreader)

        for row in csvreader:
            rows.append(row)

    table = Table(schema, rows)
    loaded_data[file_name] = table 

def get_entries(file_name):
    if file_name not in loaded_data:
        get(file_name)

    return loaded_data[file_name].entries()

def get_schema(file_name):
    if file_name not in loaded_data:
        get(file_name)

    return loaded_data[file_name].schema()