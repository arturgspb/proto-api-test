# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: v2/hello.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='v2/hello.proto',
  package='devision.hello.v2',
  syntax='proto3',
  serialized_pb=_b('\n\x0ev2/hello.proto\x12\x11\x64\x65vision.hello.v2\x1a\x1cgoogle/api/annotations.proto\"\x0e\n\x0c\x45mptyRequest\"\x0f\n\rEmptyResponse\"\x1b\n\x0b\x45\x63hoRequest\x12\x0c\n\x04name\x18\x01 \x01(\t\"/\n\x0c\x45\x63hoResponse\x12\x11\n\tserver_id\x18\x01 \x01(\t\x12\x0c\n\x04name\x18\x02 \x01(\t\"\x1b\n\x0bPingRequest\x12\x0c\n\x04ping\x18\x01 \x01(\t\"\x1c\n\x0cPingResponse\x12\x0c\n\x04ping\x18\x01 \x01(\t2\xb0\x02\n\x05Hello\x12_\n\x06Health\x12\x1f.devision.hello.v2.EmptyRequest\x1a .devision.hello.v2.EmptyResponse\"\x12\x82\xd3\xe4\x93\x02\x0c\x12\n/v2/health\x12\x62\n\x04\x45\x63ho\x12\x1e.devision.hello.v2.EchoRequest\x1a\x1f.devision.hello.v2.EchoResponse\"\x19\x82\xd3\xe4\x93\x02\x13\"\x0e/v2/hello/echo:\x01*\x12\x62\n\x04Ping\x12\x1e.devision.hello.v2.PingRequest\x1a\x1f.devision.hello.v2.PingResponse\"\x19\x82\xd3\xe4\x93\x02\x13\"\x0e/v2/hello/ping:\x01*BC\n\x14io.devision.hello.v2B\x12HelloServicesProtoP\x01\x88\x01\x01\xca\x02\x11\x44\x65vision\\Hello\\V2b\x06proto3')
  ,
  dependencies=[google_dot_api_dot_annotations__pb2.DESCRIPTOR,])




_EMPTYREQUEST = _descriptor.Descriptor(
  name='EmptyRequest',
  full_name='devision.hello.v2.EmptyRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
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
  serialized_start=67,
  serialized_end=81,
)


_EMPTYRESPONSE = _descriptor.Descriptor(
  name='EmptyResponse',
  full_name='devision.hello.v2.EmptyResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
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
  serialized_start=83,
  serialized_end=98,
)


_ECHOREQUEST = _descriptor.Descriptor(
  name='EchoRequest',
  full_name='devision.hello.v2.EchoRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='devision.hello.v2.EchoRequest.name', index=0,
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
  serialized_start=100,
  serialized_end=127,
)


_ECHORESPONSE = _descriptor.Descriptor(
  name='EchoResponse',
  full_name='devision.hello.v2.EchoResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='server_id', full_name='devision.hello.v2.EchoResponse.server_id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='name', full_name='devision.hello.v2.EchoResponse.name', index=1,
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
  serialized_start=129,
  serialized_end=176,
)


_PINGREQUEST = _descriptor.Descriptor(
  name='PingRequest',
  full_name='devision.hello.v2.PingRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='ping', full_name='devision.hello.v2.PingRequest.ping', index=0,
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
  serialized_start=178,
  serialized_end=205,
)


_PINGRESPONSE = _descriptor.Descriptor(
  name='PingResponse',
  full_name='devision.hello.v2.PingResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='ping', full_name='devision.hello.v2.PingResponse.ping', index=0,
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
  serialized_start=207,
  serialized_end=235,
)

DESCRIPTOR.message_types_by_name['EmptyRequest'] = _EMPTYREQUEST
DESCRIPTOR.message_types_by_name['EmptyResponse'] = _EMPTYRESPONSE
DESCRIPTOR.message_types_by_name['EchoRequest'] = _ECHOREQUEST
DESCRIPTOR.message_types_by_name['EchoResponse'] = _ECHORESPONSE
DESCRIPTOR.message_types_by_name['PingRequest'] = _PINGREQUEST
DESCRIPTOR.message_types_by_name['PingResponse'] = _PINGRESPONSE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

EmptyRequest = _reflection.GeneratedProtocolMessageType('EmptyRequest', (_message.Message,), dict(
  DESCRIPTOR = _EMPTYREQUEST,
  __module__ = 'v2.hello_pb2'
  # @@protoc_insertion_point(class_scope:devision.hello.v2.EmptyRequest)
  ))
_sym_db.RegisterMessage(EmptyRequest)

EmptyResponse = _reflection.GeneratedProtocolMessageType('EmptyResponse', (_message.Message,), dict(
  DESCRIPTOR = _EMPTYRESPONSE,
  __module__ = 'v2.hello_pb2'
  # @@protoc_insertion_point(class_scope:devision.hello.v2.EmptyResponse)
  ))
_sym_db.RegisterMessage(EmptyResponse)

EchoRequest = _reflection.GeneratedProtocolMessageType('EchoRequest', (_message.Message,), dict(
  DESCRIPTOR = _ECHOREQUEST,
  __module__ = 'v2.hello_pb2'
  # @@protoc_insertion_point(class_scope:devision.hello.v2.EchoRequest)
  ))
_sym_db.RegisterMessage(EchoRequest)

EchoResponse = _reflection.GeneratedProtocolMessageType('EchoResponse', (_message.Message,), dict(
  DESCRIPTOR = _ECHORESPONSE,
  __module__ = 'v2.hello_pb2'
  # @@protoc_insertion_point(class_scope:devision.hello.v2.EchoResponse)
  ))
_sym_db.RegisterMessage(EchoResponse)

PingRequest = _reflection.GeneratedProtocolMessageType('PingRequest', (_message.Message,), dict(
  DESCRIPTOR = _PINGREQUEST,
  __module__ = 'v2.hello_pb2'
  # @@protoc_insertion_point(class_scope:devision.hello.v2.PingRequest)
  ))
_sym_db.RegisterMessage(PingRequest)

PingResponse = _reflection.GeneratedProtocolMessageType('PingResponse', (_message.Message,), dict(
  DESCRIPTOR = _PINGRESPONSE,
  __module__ = 'v2.hello_pb2'
  # @@protoc_insertion_point(class_scope:devision.hello.v2.PingResponse)
  ))
_sym_db.RegisterMessage(PingResponse)


DESCRIPTOR.has_options = True
DESCRIPTOR._options = _descriptor._ParseOptions(descriptor_pb2.FileOptions(), _b('\n\024io.devision.hello.v2B\022HelloServicesProtoP\001\210\001\001\312\002\021Devision\\Hello\\V2'))

_HELLO = _descriptor.ServiceDescriptor(
  name='Hello',
  full_name='devision.hello.v2.Hello',
  file=DESCRIPTOR,
  index=0,
  options=None,
  serialized_start=238,
  serialized_end=542,
  methods=[
  _descriptor.MethodDescriptor(
    name='Health',
    full_name='devision.hello.v2.Hello.Health',
    index=0,
    containing_service=None,
    input_type=_EMPTYREQUEST,
    output_type=_EMPTYRESPONSE,
    options=_descriptor._ParseOptions(descriptor_pb2.MethodOptions(), _b('\202\323\344\223\002\014\022\n/v2/health')),
  ),
  _descriptor.MethodDescriptor(
    name='Echo',
    full_name='devision.hello.v2.Hello.Echo',
    index=1,
    containing_service=None,
    input_type=_ECHOREQUEST,
    output_type=_ECHORESPONSE,
    options=_descriptor._ParseOptions(descriptor_pb2.MethodOptions(), _b('\202\323\344\223\002\023\"\016/v2/hello/echo:\001*')),
  ),
  _descriptor.MethodDescriptor(
    name='Ping',
    full_name='devision.hello.v2.Hello.Ping',
    index=2,
    containing_service=None,
    input_type=_PINGREQUEST,
    output_type=_PINGRESPONSE,
    options=_descriptor._ParseOptions(descriptor_pb2.MethodOptions(), _b('\202\323\344\223\002\023\"\016/v2/hello/ping:\001*')),
  ),
])
_sym_db.RegisterServiceDescriptor(_HELLO)

DESCRIPTOR.services_by_name['Hello'] = _HELLO

# @@protoc_insertion_point(module_scope)
