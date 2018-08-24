from grpc_tools import protoc

protoc.main((
    '',
    '-I./protos',
    '--python_out=./src',
    '--grpc_python_out=./src',
    '--mypy_out=./src',
    './protos/hello.proto',
))
