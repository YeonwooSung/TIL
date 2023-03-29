from multiprocessing import Queue
from typing import Callable, list


def task_wrapper(pid:int, function:Callable, batch:list, queue:Queue, *args, **kwargs):
    """
    Wrapper to add progress bar update

    Parameters:
    -----------
    pid : int
        Process id
    function : Callable
        Function to apply to each element in batch
    batch : list
        List of elements to apply function to
    queue : multiprocessing.Queue
        Queue to send progress updates
    *args, **kwargs :
        Arguments to pass to function
    """
    result = []
    for example in batch:
        result.append(function(example, *args, **kwargs))
        queue.put(f'update{pid}')
    return result
