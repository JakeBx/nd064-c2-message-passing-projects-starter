# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: location-grpc.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x13location-grpc.proto\"I\n\x0fLocationMessage\x12\x11\n\tlongitude\x18\x01 \x01(\t\x12\x11\n\tperson_id\x18\x02 \x01(\x05\x12\x10\n\x08latitude\x18\x03 \x01(\t\"\x18\n\nLocationID\x12\n\n\x02id\x18\x01 \x01(\x05\x32`\n\x0fLocationService\x12,\n\x06\x43reate\x12\x10.LocationMessage\x1a\x10.LocationMessage\x12\x1f\n\x03Get\x12\x0b.LocationID\x1a\x0b.LocationIDb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'location_grpc_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _globals['_LOCATIONMESSAGE']._serialized_start=23
  _globals['_LOCATIONMESSAGE']._serialized_end=96
  _globals['_LOCATIONID']._serialized_start=98
  _globals['_LOCATIONID']._serialized_end=122
  _globals['_LOCATIONSERVICE']._serialized_start=124
  _globals['_LOCATIONSERVICE']._serialized_end=220
# @@protoc_insertion_point(module_scope)
