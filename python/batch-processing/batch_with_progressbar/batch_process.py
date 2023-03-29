from typing import Dict, Union, Callable
from  math import ceil
from threading import Thread
from multiprocessing import Manager
from joblib import Parallel, delayed

# custom modules
from .progress_bar import progress_bar
from .task_wrapper import task_wrapper


def batch_process(
    items: list,
    function: Callable,
    n_workers: int=8,
    sep_progress: bool=False,
    *args,
    **kwargs,
    ) -> list[Dict[str, Union[str, list[str]]]]:
    """
    Batch process a list of items.
    The <items> will be divided into n_workers batches which process the list individually using joblib.
    When done, all results are collected and returned as a list.

    Parameters:
    -----------
    items : list
        List of items to batch process.
        This list will be divided in n_workers batches and processed by the function.
    function : Callable
        Function used to process each row. Format needs to be:
            callable(item, *args, **kwargs).
    n_workers : int (Default: 8)
        Number of processes to start (processes).
        Generally there is an optimum between 1 <= n_workeres <= total_cpus as there is an overhead for creating separate processes.
    sep_progress : bool (Default: False)
        Show a separate progress bar for each worker.
    *args, **kwargs : -
        (named) arguments to pass to batch process function.

    Returns:
    --------
    input_items : List [ Dict [ str, Union [ str, List [ str ]]]]
        List of processed input_items with collected id, words, tokens, and labels.
    """
    # Divide data in batches
    batch_size = ceil(len(items) / n_workers)
    batches = [
        items[ix:ix+batch_size]
        for ix in range(0, len(items), batch_size)
    ]

    # Check single or multiple progress bars
    if sep_progress:
        totals = [len(batch) for batch in batches]
    else:
        totals = len(items)

    # Start progress bar in separate thread
    manager = Manager()
    queue = manager.Queue()
    try:
        progproc = Thread(target=progress_bar, args=(totals, queue))
        progproc.start()

        # Parallel process the batches
        result = Parallel(n_jobs=n_workers)(
            delayed(task_wrapper)
            (pid, function, batch, queue, *args, **kwargs)
            for pid, batch in enumerate(batches)
        )

    finally:
        # Stop the progress bar thread
        queue.put('done')
        progproc.join()

    # Flatten result
    flattened = [item for sublist in result for item in sublist]
    return flattened



if __name__ == '__main__':
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

    use_progress = False # True if you want to see the progress bar
    item_count = 1000

    items = [i for i in range(item_count)]
    result = batch_process(
        items,
        batch_process_function,
        n_workers=8,
        sep_progress=use_progress,
    )
