from grpc_tools import protoc

protoc.main((
    '',
    '-I/usr/local/include',
    '-I/Users/arturgspb/go/src',
    '-I/Users/arturgspb/go/src/github.com/grpc-ecosystem/grpc-gateway/third_party/googleapis',
    '-I./protos',
    '--python_out=./src',
    '--grpc_python_out=./src',
    '--mypy_out=./src',
    './protos/hello.proto',
))
