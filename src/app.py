import base64
import json
from concurrent import futures
import time

import grpc

from src import hello_pb2_grpc
from src import hello_pb2

_ONE_DAY_IN_SECONDS = 60 * 60 * 24


class RouteGuideServicer(hello_pb2_grpc.HelloServiceServicer):

    def Ping(self, request: hello_pb2.PingRequest, context):
        return hello_pb2.PingResponse(ping="pong!")

    def Echo(self, request: hello_pb2.EchoRequest, context):
        print("Echo req")
        user_info = None
        imd = context.invocation_metadata()
        for md in imd:
            if md.key == 'x-endpoint-api-userinfo':
                user_info = json.loads(base64.b64decode(md.value))
                print(u"md.value = %s" % str())
        print(u"user_info = %s" % str(user_info))

        email = user_info['email']

        return hello_pb2.EchoResponse(server_id="myid", name="Hello, " + request.name + ". Email: " + email)


def serve(port: int, grace_period: int):
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    hello_pb2_grpc.add_HelloServiceServicer_to_server(
        RouteGuideServicer(), server)
    server.add_insecure_port('[::]:{}'.format(port))
    server.start()

    try:
        while True:
            time.sleep(_ONE_DAY_IN_SECONDS)
    except KeyboardInterrupt:
        server.stop(grace_period)


if __name__ == '__main__':
    serve(50051, 5)
