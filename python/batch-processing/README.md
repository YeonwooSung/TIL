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

## Batch Processing in Python with joblib

Joblib is a suite of Python utilities for lightweight pipelining.
It contains unique optimizations for NumPy arrays and is built to be quick and resilient on large data.
It is released under the Berkeley Source Distribution (BSD) license.

## Batch Processing in Python with Apache Airflow

Apache Airflow is a platform to programmatically author, schedule, and monitor workflows.
It is a workflow management system that allows users to create and schedule data pipelines.

Basically, Airflow itself is not a data processing engine, but you could use the Airflow to build a pipeline that runs a data processing engine.

You could check out an example codes of Airflow [here](./airflow/).
