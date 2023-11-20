from relational_algebra import RelationalAlgebra

table_name = "organizations"
ra = RelationalAlgebra(table_name)

def load():
    ra._Load() 
    
def run_unoptimized_query():
    # Unoptimized Query 

    ra.Project(
        ra.Sort(
            ra.Scan(), 
            "Number of employees"
        ),
        ["Number of employees"]
    )

def run_optimized_query():
    # optimized Query 

    ra.SortByIndex(
        ra.Project(
            ra.Scan(),
            ["Number of employees"]
        ),
        0
    )
    
