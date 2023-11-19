from relational_algebra import RelationalAlgebra
import time

table_name = "organizations"
ra = RelationalAlgebra(table_name)

def filter_predicate(row):
    return int(row[ra._Schema().index("Founded")]) > 1990 

# Unoptimized Query 

# Project
#   Filter 
#     Sort
#       Scan 
start_time1 = time.time()

ra.Project(
        ra.Filter(
            ra.Sort(
                ra.Scan(), "Number of employees"
            ), 
            filter_predicate
        ),
        ["Name"]
)

print("--- %s seconds ---" % (time.time() - start_time1))

# optimized Query 

# Project
#   Sort
#     Filter
#       Scan 

start_time2 = time.time()

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

print("--- %s seconds ---" % (time.time() - start_time2))