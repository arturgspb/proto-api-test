from __future__ import print_function

import grpc

from src import hello_pb2_grpc
from gen import hello_pb2


def run():
    channel = grpc.insecure_channel('localhost:50051')
    stub = hello_pb2_grpc.HelloServiceStub(channel)

    resp = stub.Echo(
        hello_pb2.EchoRequest(name="Artur!")
    )
    print(resp)


if __name__ == '__main__':
    run()