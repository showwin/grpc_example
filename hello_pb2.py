# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: hello.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='hello.proto',
  package='hello',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\n\x0bhello.proto\x12\x05hello\"\x0e\n\x0cResponseType\"\r\n\x0bRequestType\"&\n\x07Product\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\r\n\x05price\x18\x02 \x01(\x05\x32y\n\x0eProductService\x12\x35\n\x0bListProduct\x12\x12.hello.RequestType\x1a\x0e.hello.Product\"\x00\x30\x01\x12\x30\n\nAddProduct\x12\x0e.hello.Product\x1a\x0e.hello.Product\"\x00\x30\x01\x62\x06proto3')
)




_RESPONSETYPE = _descriptor.Descriptor(
  name='ResponseType',
  full_name='hello.ResponseType',
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
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=22,
  serialized_end=36,
)


_REQUESTTYPE = _descriptor.Descriptor(
  name='RequestType',
  full_name='hello.RequestType',
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
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=38,
  serialized_end=51,
)


_PRODUCT = _descriptor.Descriptor(
  name='Product',
  full_name='hello.Product',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='hello.Product.name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='price', full_name='hello.Product.price', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=53,
  serialized_end=91,
)

DESCRIPTOR.message_types_by_name['ResponseType'] = _RESPONSETYPE
DESCRIPTOR.message_types_by_name['RequestType'] = _REQUESTTYPE
DESCRIPTOR.message_types_by_name['Product'] = _PRODUCT
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

ResponseType = _reflection.GeneratedProtocolMessageType('ResponseType', (_message.Message,), dict(
  DESCRIPTOR = _RESPONSETYPE,
  __module__ = 'hello_pb2'
  # @@protoc_insertion_point(class_scope:hello.ResponseType)
  ))
_sym_db.RegisterMessage(ResponseType)

RequestType = _reflection.GeneratedProtocolMessageType('RequestType', (_message.Message,), dict(
  DESCRIPTOR = _REQUESTTYPE,
  __module__ = 'hello_pb2'
  # @@protoc_insertion_point(class_scope:hello.RequestType)
  ))
_sym_db.RegisterMessage(RequestType)

Product = _reflection.GeneratedProtocolMessageType('Product', (_message.Message,), dict(
  DESCRIPTOR = _PRODUCT,
  __module__ = 'hello_pb2'
  # @@protoc_insertion_point(class_scope:hello.Product)
  ))
_sym_db.RegisterMessage(Product)



_PRODUCTSERVICE = _descriptor.ServiceDescriptor(
  name='ProductService',
  full_name='hello.ProductService',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  serialized_start=93,
  serialized_end=214,
  methods=[
  _descriptor.MethodDescriptor(
    name='ListProduct',
    full_name='hello.ProductService.ListProduct',
    index=0,
    containing_service=None,
    input_type=_REQUESTTYPE,
    output_type=_PRODUCT,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='AddProduct',
    full_name='hello.ProductService.AddProduct',
    index=1,
    containing_service=None,
    input_type=_PRODUCT,
    output_type=_PRODUCT,
    serialized_options=None,
  ),
])
_sym_db.RegisterServiceDescriptor(_PRODUCTSERVICE)

DESCRIPTOR.services_by_name['ProductService'] = _PRODUCTSERVICE

# @@protoc_insertion_point(module_scope)
