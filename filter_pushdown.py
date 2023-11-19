from relational_algebra import RelationalAlgebra
import time

table_name = "organizations"
ra = RelationalAlgebra(table_name)

def filter_predicate(row):
    return int(row[ra._Schema().index("Founded")]) > 1990 


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
