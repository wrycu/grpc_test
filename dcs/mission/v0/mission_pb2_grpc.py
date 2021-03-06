# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

from dcs.mission.v0 import mission_pb2 as dcs_dot_mission_dot_v0_dot_mission__pb2


class MissionServiceStub(object):
    """the "path" field in mission command requests and responses is a repeated
    string however "paths" doesn't make sense. therefore we will disable
    the linter pluralization checks for this file.
    protolint:disable REPEATED_FIELD_NAMES_PLURALIZED

    Contains the streaming APIs that streaming information out of the DCS server.
    """

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.StreamEvents = channel.unary_stream(
                '/dcs.mission.v0.MissionService/StreamEvents',
                request_serializer=dcs_dot_mission_dot_v0_dot_mission__pb2.StreamEventsRequest.SerializeToString,
                response_deserializer=dcs_dot_mission_dot_v0_dot_mission__pb2.StreamEventsResponse.FromString,
                )
        self.StreamUnits = channel.unary_stream(
                '/dcs.mission.v0.MissionService/StreamUnits',
                request_serializer=dcs_dot_mission_dot_v0_dot_mission__pb2.StreamUnitsRequest.SerializeToString,
                response_deserializer=dcs_dot_mission_dot_v0_dot_mission__pb2.StreamUnitsResponse.FromString,
                )
        self.GetScenarioStartTime = channel.unary_unary(
                '/dcs.mission.v0.MissionService/GetScenarioStartTime',
                request_serializer=dcs_dot_mission_dot_v0_dot_mission__pb2.GetScenarioStartTimeRequest.SerializeToString,
                response_deserializer=dcs_dot_mission_dot_v0_dot_mission__pb2.GetScenarioStartTimeResponse.FromString,
                )
        self.GetScenarioCurrentTime = channel.unary_unary(
                '/dcs.mission.v0.MissionService/GetScenarioCurrentTime',
                request_serializer=dcs_dot_mission_dot_v0_dot_mission__pb2.GetScenarioCurrentTimeRequest.SerializeToString,
                response_deserializer=dcs_dot_mission_dot_v0_dot_mission__pb2.GetScenarioCurrentTimeResponse.FromString,
                )
        self.AddMissionCommand = channel.unary_unary(
                '/dcs.mission.v0.MissionService/AddMissionCommand',
                request_serializer=dcs_dot_mission_dot_v0_dot_mission__pb2.AddMissionCommandRequest.SerializeToString,
                response_deserializer=dcs_dot_mission_dot_v0_dot_mission__pb2.AddMissionCommandResponse.FromString,
                )
        self.AddMissionCommandSubMenu = channel.unary_unary(
                '/dcs.mission.v0.MissionService/AddMissionCommandSubMenu',
                request_serializer=dcs_dot_mission_dot_v0_dot_mission__pb2.AddMissionCommandSubMenuRequest.SerializeToString,
                response_deserializer=dcs_dot_mission_dot_v0_dot_mission__pb2.AddMissionCommandSubMenuResponse.FromString,
                )
        self.RemoveMissionCommandItem = channel.unary_unary(
                '/dcs.mission.v0.MissionService/RemoveMissionCommandItem',
                request_serializer=dcs_dot_mission_dot_v0_dot_mission__pb2.RemoveMissionCommandItemRequest.SerializeToString,
                response_deserializer=dcs_dot_mission_dot_v0_dot_mission__pb2.RemoveMissionCommandItemResponse.FromString,
                )
        self.AddCoalitionCommand = channel.unary_unary(
                '/dcs.mission.v0.MissionService/AddCoalitionCommand',
                request_serializer=dcs_dot_mission_dot_v0_dot_mission__pb2.AddCoalitionCommandRequest.SerializeToString,
                response_deserializer=dcs_dot_mission_dot_v0_dot_mission__pb2.AddCoalitionCommandResponse.FromString,
                )
        self.AddCoalitionCommandSubMenu = channel.unary_unary(
                '/dcs.mission.v0.MissionService/AddCoalitionCommandSubMenu',
                request_serializer=dcs_dot_mission_dot_v0_dot_mission__pb2.AddCoalitionCommandSubMenuRequest.SerializeToString,
                response_deserializer=dcs_dot_mission_dot_v0_dot_mission__pb2.AddCoalitionCommandSubMenuResponse.FromString,
                )
        self.RemoveCoalitionCommandItem = channel.unary_unary(
                '/dcs.mission.v0.MissionService/RemoveCoalitionCommandItem',
                request_serializer=dcs_dot_mission_dot_v0_dot_mission__pb2.RemoveCoalitionCommandItemRequest.SerializeToString,
                response_deserializer=dcs_dot_mission_dot_v0_dot_mission__pb2.RemoveCoalitionCommandItemResponse.FromString,
                )
        self.AddGroupCommand = channel.unary_unary(
                '/dcs.mission.v0.MissionService/AddGroupCommand',
                request_serializer=dcs_dot_mission_dot_v0_dot_mission__pb2.AddGroupCommandRequest.SerializeToString,
                response_deserializer=dcs_dot_mission_dot_v0_dot_mission__pb2.AddGroupCommandResponse.FromString,
                )
        self.AddGroupCommandSubMenu = channel.unary_unary(
                '/dcs.mission.v0.MissionService/AddGroupCommandSubMenu',
                request_serializer=dcs_dot_mission_dot_v0_dot_mission__pb2.AddGroupCommandSubMenuRequest.SerializeToString,
                response_deserializer=dcs_dot_mission_dot_v0_dot_mission__pb2.AddGroupCommandSubMenuResponse.FromString,
                )
        self.RemoveGroupCommandItem = channel.unary_unary(
                '/dcs.mission.v0.MissionService/RemoveGroupCommandItem',
                request_serializer=dcs_dot_mission_dot_v0_dot_mission__pb2.RemoveGroupCommandItemRequest.SerializeToString,
                response_deserializer=dcs_dot_mission_dot_v0_dot_mission__pb2.RemoveGroupCommandItemResponse.FromString,
                )


class MissionServiceServicer(object):
    """the "path" field in mission command requests and responses is a repeated
    string however "paths" doesn't make sense. therefore we will disable
    the linter pluralization checks for this file.
    protolint:disable REPEATED_FIELD_NAMES_PLURALIZED

    Contains the streaming APIs that streaming information out of the DCS server.
    """

    def StreamEvents(self, request, context):
        """Streams DCS game generated Events.
        See https://wiki.hoggitworld.com/view/Category:Events
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def StreamUnits(self, request, context):
        """Streams unit updates
        Provides similar functionality as Tacview but at a much lower update rate
        so puts less load on the server. Suitable for things like online maps but
        not as a Tacview replacement.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetScenarioStartTime(self, request, context):
        """Returns the mission's in-game starttime as an ISO 8601 formatted datetime
        string.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetScenarioCurrentTime(self, request, context):
        """Returns the mission's in-game current time as an ISO 8601 formatted
        datetime string.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def AddMissionCommand(self, request, context):
        """Adds a new mission command
        See https://wiki.hoggitworld.com/view/DCS_func_addCommand
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def AddMissionCommandSubMenu(self, request, context):
        """Adds a new command sub menu
        See https://wiki.hoggitworld.com/view/DCS_func_addSubMenu
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def RemoveMissionCommandItem(self, request, context):
        """Removes a registered mission command.
        See https://wiki.hoggitworld.com/view/DCS_func_removeItem
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def AddCoalitionCommand(self, request, context):
        """Adds a new coalition command
        See https://wiki.hoggitworld.com/view/DCS_func_addCommandForCoalition
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def AddCoalitionCommandSubMenu(self, request, context):
        """Adds a new coalition command sub menu
        See https://wiki.hoggitworld.com/view/DCS_func_addSubMenuForCoalition
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def RemoveCoalitionCommandItem(self, request, context):
        """Removes a registered coalition command.
        See https://wiki.hoggitworld.com/view/DCS_func_removeItemForCoalition
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def AddGroupCommand(self, request, context):
        """Adds a new group command
        See https://wiki.hoggitworld.com/view/DCS_func_addCommandForGroup
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def AddGroupCommandSubMenu(self, request, context):
        """Adds a new group command sub menu
        See https://wiki.hoggitworld.com/view/DCS_func_addSubMenuForGroup
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def RemoveGroupCommandItem(self, request, context):
        """Removes a group coalition command.
        See https://wiki.hoggitworld.com/view/DCS_func_removeItemForGroup
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_MissionServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'StreamEvents': grpc.unary_stream_rpc_method_handler(
                    servicer.StreamEvents,
                    request_deserializer=dcs_dot_mission_dot_v0_dot_mission__pb2.StreamEventsRequest.FromString,
                    response_serializer=dcs_dot_mission_dot_v0_dot_mission__pb2.StreamEventsResponse.SerializeToString,
            ),
            'StreamUnits': grpc.unary_stream_rpc_method_handler(
                    servicer.StreamUnits,
                    request_deserializer=dcs_dot_mission_dot_v0_dot_mission__pb2.StreamUnitsRequest.FromString,
                    response_serializer=dcs_dot_mission_dot_v0_dot_mission__pb2.StreamUnitsResponse.SerializeToString,
            ),
            'GetScenarioStartTime': grpc.unary_unary_rpc_method_handler(
                    servicer.GetScenarioStartTime,
                    request_deserializer=dcs_dot_mission_dot_v0_dot_mission__pb2.GetScenarioStartTimeRequest.FromString,
                    response_serializer=dcs_dot_mission_dot_v0_dot_mission__pb2.GetScenarioStartTimeResponse.SerializeToString,
            ),
            'GetScenarioCurrentTime': grpc.unary_unary_rpc_method_handler(
                    servicer.GetScenarioCurrentTime,
                    request_deserializer=dcs_dot_mission_dot_v0_dot_mission__pb2.GetScenarioCurrentTimeRequest.FromString,
                    response_serializer=dcs_dot_mission_dot_v0_dot_mission__pb2.GetScenarioCurrentTimeResponse.SerializeToString,
            ),
            'AddMissionCommand': grpc.unary_unary_rpc_method_handler(
                    servicer.AddMissionCommand,
                    request_deserializer=dcs_dot_mission_dot_v0_dot_mission__pb2.AddMissionCommandRequest.FromString,
                    response_serializer=dcs_dot_mission_dot_v0_dot_mission__pb2.AddMissionCommandResponse.SerializeToString,
            ),
            'AddMissionCommandSubMenu': grpc.unary_unary_rpc_method_handler(
                    servicer.AddMissionCommandSubMenu,
                    request_deserializer=dcs_dot_mission_dot_v0_dot_mission__pb2.AddMissionCommandSubMenuRequest.FromString,
                    response_serializer=dcs_dot_mission_dot_v0_dot_mission__pb2.AddMissionCommandSubMenuResponse.SerializeToString,
            ),
            'RemoveMissionCommandItem': grpc.unary_unary_rpc_method_handler(
                    servicer.RemoveMissionCommandItem,
                    request_deserializer=dcs_dot_mission_dot_v0_dot_mission__pb2.RemoveMissionCommandItemRequest.FromString,
                    response_serializer=dcs_dot_mission_dot_v0_dot_mission__pb2.RemoveMissionCommandItemResponse.SerializeToString,
            ),
            'AddCoalitionCommand': grpc.unary_unary_rpc_method_handler(
                    servicer.AddCoalitionCommand,
                    request_deserializer=dcs_dot_mission_dot_v0_dot_mission__pb2.AddCoalitionCommandRequest.FromString,
                    response_serializer=dcs_dot_mission_dot_v0_dot_mission__pb2.AddCoalitionCommandResponse.SerializeToString,
            ),
            'AddCoalitionCommandSubMenu': grpc.unary_unary_rpc_method_handler(
                    servicer.AddCoalitionCommandSubMenu,
                    request_deserializer=dcs_dot_mission_dot_v0_dot_mission__pb2.AddCoalitionCommandSubMenuRequest.FromString,
                    response_serializer=dcs_dot_mission_dot_v0_dot_mission__pb2.AddCoalitionCommandSubMenuResponse.SerializeToString,
            ),
            'RemoveCoalitionCommandItem': grpc.unary_unary_rpc_method_handler(
                    servicer.RemoveCoalitionCommandItem,
                    request_deserializer=dcs_dot_mission_dot_v0_dot_mission__pb2.RemoveCoalitionCommandItemRequest.FromString,
                    response_serializer=dcs_dot_mission_dot_v0_dot_mission__pb2.RemoveCoalitionCommandItemResponse.SerializeToString,
            ),
            'AddGroupCommand': grpc.unary_unary_rpc_method_handler(
                    servicer.AddGroupCommand,
                    request_deserializer=dcs_dot_mission_dot_v0_dot_mission__pb2.AddGroupCommandRequest.FromString,
                    response_serializer=dcs_dot_mission_dot_v0_dot_mission__pb2.AddGroupCommandResponse.SerializeToString,
            ),
            'AddGroupCommandSubMenu': grpc.unary_unary_rpc_method_handler(
                    servicer.AddGroupCommandSubMenu,
                    request_deserializer=dcs_dot_mission_dot_v0_dot_mission__pb2.AddGroupCommandSubMenuRequest.FromString,
                    response_serializer=dcs_dot_mission_dot_v0_dot_mission__pb2.AddGroupCommandSubMenuResponse.SerializeToString,
            ),
            'RemoveGroupCommandItem': grpc.unary_unary_rpc_method_handler(
                    servicer.RemoveGroupCommandItem,
                    request_deserializer=dcs_dot_mission_dot_v0_dot_mission__pb2.RemoveGroupCommandItemRequest.FromString,
                    response_serializer=dcs_dot_mission_dot_v0_dot_mission__pb2.RemoveGroupCommandItemResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'dcs.mission.v0.MissionService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class MissionService(object):
    """the "path" field in mission command requests and responses is a repeated
    string however "paths" doesn't make sense. therefore we will disable
    the linter pluralization checks for this file.
    protolint:disable REPEATED_FIELD_NAMES_PLURALIZED

    Contains the streaming APIs that streaming information out of the DCS server.
    """

    @staticmethod
    def StreamEvents(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_stream(request, target, '/dcs.mission.v0.MissionService/StreamEvents',
            dcs_dot_mission_dot_v0_dot_mission__pb2.StreamEventsRequest.SerializeToString,
            dcs_dot_mission_dot_v0_dot_mission__pb2.StreamEventsResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def StreamUnits(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_stream(request, target, '/dcs.mission.v0.MissionService/StreamUnits',
            dcs_dot_mission_dot_v0_dot_mission__pb2.StreamUnitsRequest.SerializeToString,
            dcs_dot_mission_dot_v0_dot_mission__pb2.StreamUnitsResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetScenarioStartTime(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/dcs.mission.v0.MissionService/GetScenarioStartTime',
            dcs_dot_mission_dot_v0_dot_mission__pb2.GetScenarioStartTimeRequest.SerializeToString,
            dcs_dot_mission_dot_v0_dot_mission__pb2.GetScenarioStartTimeResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetScenarioCurrentTime(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/dcs.mission.v0.MissionService/GetScenarioCurrentTime',
            dcs_dot_mission_dot_v0_dot_mission__pb2.GetScenarioCurrentTimeRequest.SerializeToString,
            dcs_dot_mission_dot_v0_dot_mission__pb2.GetScenarioCurrentTimeResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def AddMissionCommand(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/dcs.mission.v0.MissionService/AddMissionCommand',
            dcs_dot_mission_dot_v0_dot_mission__pb2.AddMissionCommandRequest.SerializeToString,
            dcs_dot_mission_dot_v0_dot_mission__pb2.AddMissionCommandResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def AddMissionCommandSubMenu(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/dcs.mission.v0.MissionService/AddMissionCommandSubMenu',
            dcs_dot_mission_dot_v0_dot_mission__pb2.AddMissionCommandSubMenuRequest.SerializeToString,
            dcs_dot_mission_dot_v0_dot_mission__pb2.AddMissionCommandSubMenuResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def RemoveMissionCommandItem(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/dcs.mission.v0.MissionService/RemoveMissionCommandItem',
            dcs_dot_mission_dot_v0_dot_mission__pb2.RemoveMissionCommandItemRequest.SerializeToString,
            dcs_dot_mission_dot_v0_dot_mission__pb2.RemoveMissionCommandItemResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def AddCoalitionCommand(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/dcs.mission.v0.MissionService/AddCoalitionCommand',
            dcs_dot_mission_dot_v0_dot_mission__pb2.AddCoalitionCommandRequest.SerializeToString,
            dcs_dot_mission_dot_v0_dot_mission__pb2.AddCoalitionCommandResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def AddCoalitionCommandSubMenu(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/dcs.mission.v0.MissionService/AddCoalitionCommandSubMenu',
            dcs_dot_mission_dot_v0_dot_mission__pb2.AddCoalitionCommandSubMenuRequest.SerializeToString,
            dcs_dot_mission_dot_v0_dot_mission__pb2.AddCoalitionCommandSubMenuResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def RemoveCoalitionCommandItem(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/dcs.mission.v0.MissionService/RemoveCoalitionCommandItem',
            dcs_dot_mission_dot_v0_dot_mission__pb2.RemoveCoalitionCommandItemRequest.SerializeToString,
            dcs_dot_mission_dot_v0_dot_mission__pb2.RemoveCoalitionCommandItemResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def AddGroupCommand(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/dcs.mission.v0.MissionService/AddGroupCommand',
            dcs_dot_mission_dot_v0_dot_mission__pb2.AddGroupCommandRequest.SerializeToString,
            dcs_dot_mission_dot_v0_dot_mission__pb2.AddGroupCommandResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def AddGroupCommandSubMenu(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/dcs.mission.v0.MissionService/AddGroupCommandSubMenu',
            dcs_dot_mission_dot_v0_dot_mission__pb2.AddGroupCommandSubMenuRequest.SerializeToString,
            dcs_dot_mission_dot_v0_dot_mission__pb2.AddGroupCommandSubMenuResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def RemoveGroupCommandItem(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/dcs.mission.v0.MissionService/RemoveGroupCommandItem',
            dcs_dot_mission_dot_v0_dot_mission__pb2.RemoveGroupCommandItemRequest.SerializeToString,
            dcs_dot_mission_dot_v0_dot_mission__pb2.RemoveGroupCommandItemResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
