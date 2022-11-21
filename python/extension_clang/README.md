# Extend Python with C/C++ code

## Setup

[setup.py](./setup.py) is a simple example of setup file for the C/C++ based python package.

By executing the given setup file, you could build the Cython package for distribution.

```bash
$ python3 setup.py build
```

## Benefits of using C/C++ extensions

1. Improve performance by implementing extermely heavy functionalities with C/C++.

2. Ignore GIL in Cython threading model

3. Integrate with the source codes that are written in C/C++, etc

4. Integrate with 3rd party DLLs

5. Can customize new data types efficiently
