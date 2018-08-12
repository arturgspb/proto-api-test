from grpc_tools import protoc

protoc.main((
    '',
    '-I./protos',
    '--python_out=./gen',
    '--grpc_python_out=./gen',
    '--mypy_out=./gen',
    './protos/hello.proto',
))
