# gRPC - bidirectional

## Instructions for compiling proto file

convert proto file to python code:

```
$ python -m grpc_tools.protoc --proto_path=.  ./bidirectional.proto --python_out=. --grpc_python_out=.
```
