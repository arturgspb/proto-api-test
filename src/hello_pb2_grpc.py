# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
import grpc

import hello_pb2 as hello__pb2


class HelloServiceStub(object):
  # missing associated documentation comment in .proto file
  pass

  def __init__(self, channel):
    """Constructor.

    Args:
      channel: A grpc.Channel.
    """
    self.Echo = channel.unary_unary(
        '/helloapi.HelloService/Echo',
        request_serializer=hello__pb2.EchoRequest.SerializeToString,
        response_deserializer=hello__pb2.EchoResponse.FromString,
        )
    self.Ping = channel.unary_unary(
        '/helloapi.HelloService/Ping',
        request_serializer=hello__pb2.PingRequest.SerializeToString,
        response_deserializer=hello__pb2.PingResponse.FromString,
        )


class HelloServiceServicer(object):
  # missing associated documentation comment in .proto file
  pass

  def Echo(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def Ping(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')


def add_HelloServiceServicer_to_server(servicer, server):
  rpc_method_handlers = {
      'Echo': grpc.unary_unary_rpc_method_handler(
          servicer.Echo,
          request_deserializer=hello__pb2.EchoRequest.FromString,
          response_serializer=hello__pb2.EchoResponse.SerializeToString,
      ),
      'Ping': grpc.unary_unary_rpc_method_handler(
          servicer.Ping,
          request_deserializer=hello__pb2.PingRequest.FromString,
          response_serializer=hello__pb2.PingResponse.SerializeToString,
      ),
  }
  generic_handler = grpc.method_handlers_generic_handler(
      'helloapi.HelloService', rpc_method_handlers)
  server.add_generic_rpc_handlers((generic_handler,))
