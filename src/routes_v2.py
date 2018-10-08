from metasdk.apiserver import Api

from src.v2 import hello_pb2_grpc, hello_pb2


class RouteGuideServicerV2(hello_pb2_grpc.HelloServicer):
    def Health(self, request, context):
        return hello_pb2.EmptyResponse()

    @Api(
        scopes=["meta.dev"]
    )
    def Ping(self, request: hello_pb2.PingRequest, context):
        return hello_pb2.PingResponse(ping="pong!")

    @Api(
        scopes=["meta.dev"]
    )
    def Echo(self, request: hello_pb2.EchoRequest, context):
        return hello_pb2.EchoResponse(server_id="myid", name="Hello, " + request.name)

def reg_server_v2(server):
    hello_pb2_grpc.add_HelloServicer_to_server(RouteGuideServicerV2(), server)
