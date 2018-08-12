from concurrent import futures
import time

import grpc

from src import hello_pb2_grpc
from src import hello_pb2

_ONE_DAY_IN_SECONDS = 60 * 60 * 24


class RouteGuideServicer(hello_pb2_grpc.HelloServiceServicer):

    def Echo(self, request: hello_pb2.EchoRequest, context):
        return hello_pb2.EchoResponse(server_id="myid", name="Hello, " + request.name)


def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    hello_pb2_grpc.add_HelloServiceServicer_to_server(
        RouteGuideServicer(), server)
    server.add_insecure_port('[::]:50051')
    server.start()
    try:
        while True:
            time.sleep(_ONE_DAY_IN_SECONDS)
    except KeyboardInterrupt:
        server.stop(0)


if __name__ == '__main__':
    serve()
