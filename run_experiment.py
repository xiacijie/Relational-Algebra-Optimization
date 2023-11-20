import filter_pushdown as fp 
import constant_folding as cf 
import sort_elimination as se 
import projection_pushdown as pp

import data_loader

import time 

RUNS = 1

opts = [fp, cf, se, pp]

for op in opts:
    optimized_time = 0
    unoptimized_time = 0

    # load the data into memory
    op.load() 

    for i in range(RUNS):
        t1 = time.time()
        op.run_unoptimized_query()
        unoptimized_time += time.time() - t1 

        t2 = time.time()
        op.run_optimized_query()
        optimized_time += time.time() - t2 
    
    avg_opt_time = optimized_time / RUNS 
    avg_unopt_time = unoptimized_time / RUNS 

    print(op.__name__, avg_unopt_time, avg_opt_time)

