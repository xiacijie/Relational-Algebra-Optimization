from relational_algebra import RelationalAlgebra

table_name = "organizations"
ra = RelationalAlgebra(table_name)

def filter_predicate(row):
    return int(row[ra._Schema().index("Founded")]) > 2000 

def load():
    ra._Load() 
    
def run_unoptimized_query():
    # Unoptimized Query 

    # Project
    #   Filter 
    #     Sort
    #       Scan 

    ra.Project(
        ra.Filter(
            ra.Sort(
                ra.Scan(), "Number of employees"
            ), 
            filter_predicate
        ),
        ["Name"]
    )

def run_optimized_query():
    # optimized Query 

    # Project
    #   Sort
    #     Filter
    #       Scan 

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
