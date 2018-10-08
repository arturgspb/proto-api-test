import base64
import json

from src.v1 import hello_pb2_grpc, hello_pb2


class RouteGuideServicerV1(hello_pb2_grpc.HelloServicer):
    def Health(self, request, context):
        return hello_pb2.EmptyResponse()

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

def reg_server_v1(server):
    hello_pb2_grpc.add_HelloServicer_to_server(RouteGuideServicerV1(), server)
