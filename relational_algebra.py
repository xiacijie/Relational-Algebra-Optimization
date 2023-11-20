import data_loader

class RelationalAlgebra:
    def __init__(self, table_name) -> None:
        self.table_name = table_name

    def _FileName(self):
        return "./dataset/" + self.table_name + ".csv"

    def _Schema(self):
        return data_loader.get_schema(self._FileName())

    def _FieldIndexes(self, fields):
        schema = self._Schema()
        fields_indexes = []

        for field in fields:
            fields_indexes.append(schema.index(field))

        return fields_indexes

    def _Load(self):
        data_loader.get(self._FileName())
        
    def Scan(self):
        return data_loader.get_entries(self._FileName())

    def Project(self, input, fields):
        fields_indexes = self._FieldIndexes(fields)

        output = []

        for inp in input:
            row = []
            for i in fields_indexes:
                row.append(inp[i])
            output.append(row)

        return output 

    def Filter(self, input, predicate):
        output = []

        for inp in input:
            if predicate(inp):
                output.append(inp)

        return output 

    def Sort(self, input, field, DES=False):
        schema = self._Schema()
        return sorted(input, key=lambda x: x[schema.index(field)], reverse=DES)
    
    def SortByIndex(self, input, idx, DES=False):
        return sorted(input, key=lambda x: x[idx], reverse=DES)
    

    def Union(self, )