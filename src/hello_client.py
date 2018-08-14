from __future__ import print_function

import grpc

from src import hello_pb2_grpc
from src import hello_pb2


def run():
    # channel = grpc.insecure_channel('localhost:12345')
    # channel = grpc.insecure_channel('localhost:50051')
    channel = grpc.insecure_channel('apiproxyt.apis.kb2.1ad.ru:50051')
    # channel = grpc.insecure_channel('n2.adp.vmc.loc:31846')
    stub = hello_pb2_grpc.HelloServiceStub(channel)

    resp = stub.Echo(
        hello_pb2.EchoRequest(name="Artur!"),
        metadata=[("foo", "bar")]
    )
    print(resp)


if __name__ == '__main__':
    run()