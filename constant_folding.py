from relational_algebra import RelationalAlgebra

table_name = "organizations"
ra = RelationalAlgebra(table_name)

def load():
    ra._Load()

def filter_predicate(row):
    return int(row[ra._Schema().index("Number of employees")]) < 5*4*3*2*1

def filter_predicate_constant(row):
    return int(row[ra._Schema().index("Number of employees")]) < 120

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
        ra.Sort(
            ra.Filter(
                ra.Scan(),
                filter_predicate_constant
            ),
            "Number of employees"
        ),
        ["Name"]
    )
