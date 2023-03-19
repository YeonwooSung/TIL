from joblib import Parallel, delayed
from tqdm import tqdm


def batch_process_function(row, order, payload):
    """
    Simulate process function
    
    Row and payload are ignored.
    
    Approximate pi
    """
    k, pi = 1, 0
    for i in range(10**6):
        if i % 2 == 0: # even
            pi += 4 / k
        else:  # odd 
            pi -= 4 / k 
        k += 2
    return pi


# Settings
order=6
N = 1_000
items = range(N)

# Serial run
result = [batch_process_function(row, order, None) for row in items]

# Parallel using joblib and a progress bar using tqdm
result = Parallel(n_jobs=8)(
    delayed(batch_process_function)
    (row, order, None) 
    for row in tqdm(items)
)
