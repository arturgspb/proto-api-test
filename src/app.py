from concurrent import futures
import time

import grpc

print("Start server 1")

time.sleep(1)

from src import hello_pb2_grpc
from src import hello_pb2

print("Start server 2")
time.sleep(1)

_ONE_DAY_IN_SECONDS = 60 * 60 * 24


class RouteGuideServicer(hello_pb2_grpc.HelloServiceServicer):

    def Echo(self, request: hello_pb2.EchoRequest, context):
        print("Echo req")
        return hello_pb2.EchoResponse(server_id="myid", name="Hello, " + request.name)


def serve(port: int, grace_period: int):
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    hello_pb2_grpc.add_HelloServiceServicer_to_server(
        RouteGuideServicer(), server)
    server.add_insecure_port('[::]:{}'.format(port))
    print("Start server 4")
    time.sleep(5)

    server.start()
    print("Start server 5")

    try:
        while True:
            time.sleep(_ONE_DAY_IN_SECONDS)
    except KeyboardInterrupt:
        server.stop(grace_period)


if __name__ == '__main__':
    print("Start server 3")
    time.sleep(1)

    serve(50051, 5)
