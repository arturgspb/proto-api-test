# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: hello.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='hello.proto',
  package='helloapi',
  syntax='proto3',
  serialized_pb=_b('\n\x0bhello.proto\x12\x08helloapi\"\x1b\n\x0b\x45\x63hoRequest\x12\x0c\n\x04name\x18\x01 \x01(\t\"/\n\x0c\x45\x63hoResponse\x12\x11\n\tserver_id\x18\x01 \x01(\t\x12\x0c\n\x04name\x18\x02 \x01(\t\"\x1b\n\x0bPingRequest\x12\x0c\n\x04ping\x18\x01 \x01(\t\"\x1c\n\x0cPingResponse\x12\x0c\n\x04ping\x18\x01 \x01(\t2\x80\x01\n\x0cHelloService\x12\x37\n\x04\x45\x63ho\x12\x15.helloapi.EchoRequest\x1a\x16.helloapi.EchoResponse\"\x00\x12\x37\n\x04Ping\x12\x15.helloapi.PingRequest\x1a\x16.helloapi.PingResponse\"\x00\x42\x02P\x01\x62\x06proto3')
)




_ECHOREQUEST = _descriptor.Descriptor(
  name='EchoRequest',
  full_name='helloapi.EchoRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='helloapi.EchoRequest.name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=25,
  serialized_end=52,
)


_ECHORESPONSE = _descriptor.Descriptor(
  name='EchoResponse',
  full_name='helloapi.EchoResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='server_id', full_name='helloapi.EchoResponse.server_id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='name', full_name='helloapi.EchoResponse.name', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=54,
  serialized_end=101,
)


_PINGREQUEST = _descriptor.Descriptor(
  name='PingRequest',
  full_name='helloapi.PingRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='ping', full_name='helloapi.PingRequest.ping', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=103,
  serialized_end=130,
)


_PINGRESPONSE = _descriptor.Descriptor(
  name='PingResponse',
  full_name='helloapi.PingResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='ping', full_name='helloapi.PingResponse.ping', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=132,
  serialized_end=160,
)

DESCRIPTOR.message_types_by_name['EchoRequest'] = _ECHOREQUEST
DESCRIPTOR.message_types_by_name['EchoResponse'] = _ECHORESPONSE
DESCRIPTOR.message_types_by_name['PingRequest'] = _PINGREQUEST
DESCRIPTOR.message_types_by_name['PingResponse'] = _PINGRESPONSE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

EchoRequest = _reflection.GeneratedProtocolMessageType('EchoRequest', (_message.Message,), dict(
  DESCRIPTOR = _ECHOREQUEST,
  __module__ = 'hello_pb2'
  # @@protoc_insertion_point(class_scope:helloapi.EchoRequest)
  ))
_sym_db.RegisterMessage(EchoRequest)

EchoResponse = _reflection.GeneratedProtocolMessageType('EchoResponse', (_message.Message,), dict(
  DESCRIPTOR = _ECHORESPONSE,
  __module__ = 'hello_pb2'
  # @@protoc_insertion_point(class_scope:helloapi.EchoResponse)
  ))
_sym_db.RegisterMessage(EchoResponse)

PingRequest = _reflection.GeneratedProtocolMessageType('PingRequest', (_message.Message,), dict(
  DESCRIPTOR = _PINGREQUEST,
  __module__ = 'hello_pb2'
  # @@protoc_insertion_point(class_scope:helloapi.PingRequest)
  ))
_sym_db.RegisterMessage(PingRequest)

PingResponse = _reflection.GeneratedProtocolMessageType('PingResponse', (_message.Message,), dict(
  DESCRIPTOR = _PINGRESPONSE,
  __module__ = 'hello_pb2'
  # @@protoc_insertion_point(class_scope:helloapi.PingResponse)
  ))
_sym_db.RegisterMessage(PingResponse)


DESCRIPTOR.has_options = True
DESCRIPTOR._options = _descriptor._ParseOptions(descriptor_pb2.FileOptions(), _b('P\001'))

_HELLOSERVICE = _descriptor.ServiceDescriptor(
  name='HelloService',
  full_name='helloapi.HelloService',
  file=DESCRIPTOR,
  index=0,
  options=None,
  serialized_start=163,
  serialized_end=291,
  methods=[
  _descriptor.MethodDescriptor(
    name='Echo',
    full_name='helloapi.HelloService.Echo',
    index=0,
    containing_service=None,
    input_type=_ECHOREQUEST,
    output_type=_ECHORESPONSE,
    options=None,
  ),
  _descriptor.MethodDescriptor(
    name='Ping',
    full_name='helloapi.HelloService.Ping',
    index=1,
    containing_service=None,
    input_type=_PINGREQUEST,
    output_type=_PINGRESPONSE,
    options=None,
  ),
])
_sym_db.RegisterServiceDescriptor(_HELLOSERVICE)

DESCRIPTOR.services_by_name['HelloService'] = _HELLOSERVICE

# @@protoc_insertion_point(module_scope)
