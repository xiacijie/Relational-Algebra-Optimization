from relational_algebra import RelationalAlgebra

table_name = "organizations"
ra = RelationalAlgebra(table_name)

def filter_predicate(row):
    return int(row[ra._Schema().index("Founded")]) > 1990 

def load():
    ra._Load()
    
def run_unoptimized_query():
    # unoptimized Query 

    ra.Project(
        ra.Sort(
            ra.Filter(
                ra.Scan(),
                filter_predicate
            ),
            "Number of employees"
        ),
        ["Name"]
    )


def run_optimized_query():
    # optimized Query 

    ra.Project(
        ra.Filter(
            ra.Scan(),
            filter_predicate
        ),
        ["Name"]
    )