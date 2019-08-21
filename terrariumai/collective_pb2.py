# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: collective.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='collective.proto',
  package='endpoints.terrariumai.collective',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\n\x10\x63ollective.proto\x12 endpoints.terrariumai.collective\"%\n\x06\x45ntity\x12\n\n\x02id\x18\x01 \x01(\t\x12\x0f\n\x07\x63lassID\x18\x02 \x01(\r\"\x8c\x01\n\x06\x45\x66\x66\x65\x63t\x12?\n\x07\x63lassID\x18\x01 \x01(\x0e\x32..endpoints.terrariumai.collective.Effect.Class\x12\r\n\x05value\x18\x02 \x01(\r\x12\x10\n\x08strength\x18\x03 \x01(\r\" \n\x05\x43lass\x12\x08\n\x04NONE\x10\x00\x12\r\n\tPHEROMONE\x10\x01\"\xbc\x01\n\x0bObservation\x12\x0f\n\x07isAlive\x18\x01 \x01(\x08\x12\x0e\n\x06\x65nergy\x18\x02 \x01(\r\x12\x0e\n\x06health\x18\x03 \x01(\r\x12\n\n\x02id\x18\x04 \x01(\t\x12\x37\n\x05sight\x18\x05 \x03(\x0b\x32(.endpoints.terrariumai.collective.Entity\x12\x37\n\x05smell\x18\x06 \x03(\x0b\x32(.endpoints.terrariumai.collective.Effect\"7\n\x06\x41\x63tion\x12\n\n\x02id\x18\x01 \x01(\t\x12\x0e\n\x06\x61\x63tion\x18\x02 \x01(\r\x12\x11\n\tdirection\x18\x03 \x01(\r\"X\n\x11ObservationPacket\x12\x43\n\x0cobservations\x18\x01 \x03(\x0b\x32-.endpoints.terrariumai.collective.Observation\"I\n\x0c\x41\x63tionPacket\x12\x39\n\x07\x61\x63tions\x18\x01 \x03(\x0b\x32(.endpoints.terrariumai.collective.Action2\x8d\x01\n\nCollective\x12\x7f\n\x12\x43onnectRemoteModel\x12..endpoints.terrariumai.collective.ActionPacket\x1a\x33.endpoints.terrariumai.collective.ObservationPacket\"\x00(\x01\x30\x01\x62\x06proto3')
)



_EFFECT_CLASS = _descriptor.EnumDescriptor(
  name='Class',
  full_name='endpoints.terrariumai.collective.Effect.Class',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='NONE', index=0, number=0,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='PHEROMONE', index=1, number=1,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=202,
  serialized_end=234,
)
_sym_db.RegisterEnumDescriptor(_EFFECT_CLASS)


_ENTITY = _descriptor.Descriptor(
  name='Entity',
  full_name='endpoints.terrariumai.collective.Entity',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='endpoints.terrariumai.collective.Entity.id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='classID', full_name='endpoints.terrariumai.collective.Entity.classID', index=1,
      number=2, type=13, cpp_type=3, label=1,
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
  serialized_start=54,
  serialized_end=91,
)


_EFFECT = _descriptor.Descriptor(
  name='Effect',
  full_name='endpoints.terrariumai.collective.Effect',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='classID', full_name='endpoints.terrariumai.collective.Effect.classID', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='value', full_name='endpoints.terrariumai.collective.Effect.value', index=1,
      number=2, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='strength', full_name='endpoints.terrariumai.collective.Effect.strength', index=2,
      number=3, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _EFFECT_CLASS,
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=94,
  serialized_end=234,
)


_OBSERVATION = _descriptor.Descriptor(
  name='Observation',
  full_name='endpoints.terrariumai.collective.Observation',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='isAlive', full_name='endpoints.terrariumai.collective.Observation.isAlive', index=0,
      number=1, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='energy', full_name='endpoints.terrariumai.collective.Observation.energy', index=1,
      number=2, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='health', full_name='endpoints.terrariumai.collective.Observation.health', index=2,
      number=3, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='id', full_name='endpoints.terrariumai.collective.Observation.id', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='sight', full_name='endpoints.terrariumai.collective.Observation.sight', index=4,
      number=5, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='smell', full_name='endpoints.terrariumai.collective.Observation.smell', index=5,
      number=6, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
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
  serialized_start=237,
  serialized_end=425,
)


_ACTION = _descriptor.Descriptor(
  name='Action',
  full_name='endpoints.terrariumai.collective.Action',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='endpoints.terrariumai.collective.Action.id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='action', full_name='endpoints.terrariumai.collective.Action.action', index=1,
      number=2, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='direction', full_name='endpoints.terrariumai.collective.Action.direction', index=2,
      number=3, type=13, cpp_type=3, label=1,
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
  serialized_start=427,
  serialized_end=482,
)


_OBSERVATIONPACKET = _descriptor.Descriptor(
  name='ObservationPacket',
  full_name='endpoints.terrariumai.collective.ObservationPacket',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='observations', full_name='endpoints.terrariumai.collective.ObservationPacket.observations', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
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
  serialized_start=484,
  serialized_end=572,
)


_ACTIONPACKET = _descriptor.Descriptor(
  name='ActionPacket',
  full_name='endpoints.terrariumai.collective.ActionPacket',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='actions', full_name='endpoints.terrariumai.collective.ActionPacket.actions', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
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
  serialized_start=574,
  serialized_end=647,
)

_EFFECT.fields_by_name['classID'].enum_type = _EFFECT_CLASS
_EFFECT_CLASS.containing_type = _EFFECT
_OBSERVATION.fields_by_name['sight'].message_type = _ENTITY
_OBSERVATION.fields_by_name['smell'].message_type = _EFFECT
_OBSERVATIONPACKET.fields_by_name['observations'].message_type = _OBSERVATION
_ACTIONPACKET.fields_by_name['actions'].message_type = _ACTION
DESCRIPTOR.message_types_by_name['Entity'] = _ENTITY
DESCRIPTOR.message_types_by_name['Effect'] = _EFFECT
DESCRIPTOR.message_types_by_name['Observation'] = _OBSERVATION
DESCRIPTOR.message_types_by_name['Action'] = _ACTION
DESCRIPTOR.message_types_by_name['ObservationPacket'] = _OBSERVATIONPACKET
DESCRIPTOR.message_types_by_name['ActionPacket'] = _ACTIONPACKET
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Entity = _reflection.GeneratedProtocolMessageType('Entity', (_message.Message,), {
  'DESCRIPTOR' : _ENTITY,
  '__module__' : 'collective_pb2'
  # @@protoc_insertion_point(class_scope:endpoints.terrariumai.collective.Entity)
  })
_sym_db.RegisterMessage(Entity)

Effect = _reflection.GeneratedProtocolMessageType('Effect', (_message.Message,), {
  'DESCRIPTOR' : _EFFECT,
  '__module__' : 'collective_pb2'
  # @@protoc_insertion_point(class_scope:endpoints.terrariumai.collective.Effect)
  })
_sym_db.RegisterMessage(Effect)

Observation = _reflection.GeneratedProtocolMessageType('Observation', (_message.Message,), {
  'DESCRIPTOR' : _OBSERVATION,
  '__module__' : 'collective_pb2'
  # @@protoc_insertion_point(class_scope:endpoints.terrariumai.collective.Observation)
  })
_sym_db.RegisterMessage(Observation)

Action = _reflection.GeneratedProtocolMessageType('Action', (_message.Message,), {
  'DESCRIPTOR' : _ACTION,
  '__module__' : 'collective_pb2'
  # @@protoc_insertion_point(class_scope:endpoints.terrariumai.collective.Action)
  })
_sym_db.RegisterMessage(Action)

ObservationPacket = _reflection.GeneratedProtocolMessageType('ObservationPacket', (_message.Message,), {
  'DESCRIPTOR' : _OBSERVATIONPACKET,
  '__module__' : 'collective_pb2'
  # @@protoc_insertion_point(class_scope:endpoints.terrariumai.collective.ObservationPacket)
  })
_sym_db.RegisterMessage(ObservationPacket)

ActionPacket = _reflection.GeneratedProtocolMessageType('ActionPacket', (_message.Message,), {
  'DESCRIPTOR' : _ACTIONPACKET,
  '__module__' : 'collective_pb2'
  # @@protoc_insertion_point(class_scope:endpoints.terrariumai.collective.ActionPacket)
  })
_sym_db.RegisterMessage(ActionPacket)



_COLLECTIVE = _descriptor.ServiceDescriptor(
  name='Collective',
  full_name='endpoints.terrariumai.collective.Collective',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  serialized_start=650,
  serialized_end=791,
  methods=[
  _descriptor.MethodDescriptor(
    name='ConnectRemoteModel',
    full_name='endpoints.terrariumai.collective.Collective.ConnectRemoteModel',
    index=0,
    containing_service=None,
    input_type=_ACTIONPACKET,
    output_type=_OBSERVATIONPACKET,
    serialized_options=None,
  ),
])
_sym_db.RegisterServiceDescriptor(_COLLECTIVE)

DESCRIPTOR.services_by_name['Collective'] = _COLLECTIVE

# @@protoc_insertion_point(module_scope)
