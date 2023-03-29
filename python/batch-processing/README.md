# Batch Processing in Python

Batch Processing is essential for corporations and organizations to effectively manage massive volumes of data.
It’s particularly well-suited to managing regular, repetitive tasks.

## What is Batch Processing?

Batch Processing is a technique for processing large amounts of data in a repeatable manner.
When computational resources are available, the batch technique allows users to process data with little or no human intervention.
Simply described, batch processing is the method through which a computer completes batches of work in a nonstop, sequential manner, typically simultaneously.
It’s also a command that guarantees huge jobs are broken down into smaller chunks for debugging efficiency.

## Batch ETL Processing

Batch ETL Processing entails users collecting and storing data in batches during the course of a “batch window”.
This saves time and enhances data processing efficiency, allowing organizations and businesses to handle enormous volumes of data and analyze it rapidly.

## What are the Benefits of Python Batch Processing?

Businesses use Batch Processing systems for a variety of reasons.
When choosing new software for their company, business owners should consider the overall impact.

Some of the advantages of Python Batch Processing are:

    * Speed & Low Costs: Batch Processing can lessen a company’s dependency on other pricey pieces of technology, making it a comparatively low-cost option that saves money and time. Batch procedures are executed most efficiently and feasibly without the risk of user mistakes. As a result, managers have more time to focus on day-to-day operations and can analyze data more quickly and accurately.

    * Offline Features: Batch Processing systems work in a stand-alone mode. This process is still going strong at the end of the day. To prevent overloading a system and disturbing regular tasks, Managers can restrict when a process begins. The software can be configured to execute specific batches overnight, which is a practical option for firms that don’t want jobs like automated downloads to disturb their daily operations.

    * Efficiency: When computers or other resources are readily accessible, Batch Processing allows a corporation to handle jobs. Companies can plan batch operations for activities that aren’t as urgent and prioritize time-sensitive jobs. Batch systems can also run in the background to reduce processor burden.

    * Simplicity: Batch Processing, in comparison to Stream Processing, is a less sophisticated system that does not require particular hardware or system support for data entry. It requires less maintenance after it is set up than a stream processing system.

## Batch Processing in Python with joblib

Joblib is a suite of Python utilities for lightweight pipelining.
It contains unique optimizations for NumPy arrays and is built to be quick and resilient on large data.
It is released under the Berkeley Source Distribution (BSD) license.

Some of the key features of Joblib are:

    - Transparent Disk-Caching of Functions & Lazy Re-Evaluation: A memoize or make-like feature for Python functions that work with any Python object, including very big NumPy arrays. By expressing the operations as a collection of steps with well-defined inputs and outputs: Python functions, you can separate persistence and flow-execution logic from the domain logic or algorithmic code. Joblib can save their computation to disc and repeat it only if required.
    - Simple Parallel Computing: Joblib makes it easy to write readable parallel code and easily debug it.
    - Fast Compressed Persistence: An alternative for a pickle that works well with Python objects that contain a lot of data ( joblib.dump & joblib.load ).

[Here](./simple-joblib-pipeline.py) is a simple example of using joblib to build a pipeline.

The given example file runs the simple PI calculation function called `batch_process_function` in 2 different ways:

    - Sequentially
    - Parallelly

If you run the example file with time checking, you could see that the parallel way is much faster than the sequential way.

| Sequential | Parallel |
|------------|----------|
| 1m 34s | 0m 21.7s |

### Is joblib.Parallel a "real" parallel processing?

If you visit the [official github repo of joblib](https://github.com/joblib/joblib), you could find that the `joblib.Parallel` uses `threading` for parallel processing with `multiprocessing.pool.ThreadPool` as the default backend.
This means that the `joblib.Parallel` is not a "real" parallel processing, and it is affected by the GIL (Global Interpreter Lock) of Python.

However, the Python threading could be a good solution for IO-bound tasks, and it does not suffer from the complex IPC (Inter-Process Communication) of multiprocessing.
So, if you are trying to make a IO-bounded batch processing task, using the `joblib.Parallel` could be a good choice.

### Use multiprocessing for "real" parallel processing

The multi-processing could be a good solution for CPU-bound tasks, and it does not suffer from the GIL of Python.
So, if you are trying to make a CPU-bounded batch processing task, using the `multiprocessing` could be a good choice.

However, if you are trying to make a IO-bounded batch processing task, using the `multiprocessing` could be a bad choice, because it is affected by the complex IPC of multiprocessing.

Also, serializing and deserializing data in the multiprocessing could be a bottleneck for the performance of the multiprocessing.
This is because the data needs to be serialized and deserialized when it is passed between processes.
Serializing and deserializing a large data requires additional memory and disk, which makes the machine to use more I/O resources.

If you abuse the `multiprocessing`, for example, passing an extremely large data as required arguments to the `multiprocessing.Pool`, it could be a bad choice.
In this case, the multiprocessing will copy that large data for each process, and pass the copied data to each process with serialization and deserialization.

The solution for overcoming this problem is simple: reduce the amount of serializations. Instead of serializing for each item, we will create an additional wrapper function that works on the batch inside the process. This results in only serializing the data once for each process.

You could find the example codes of using multiprocessing with the wrapper function solution [here](./batch_with_progressbar/).

To run the example:

```bash
$ cd batch_with_progressbar
$ python batch_process.py
```

## Batch Processing in Python with Apache Airflow

Apache Airflow is a platform to programmatically author, schedule, and monitor workflows.
It is a workflow management system that allows users to create and schedule data pipelines.

Basically, Airflow itself is not a data processing engine, but you could use the Airflow to build a pipeline that runs a data processing engine.

You could check out an example codes of Airflow [here](./airflow/).

## References

- [Python Batch Processing](https://hevodata.com/learn/python-batch-processing/)
- [Parallel batch processing in Python](https://towardsdatascience.com/parallel-batch-processing-in-python-8dcce607d226)
