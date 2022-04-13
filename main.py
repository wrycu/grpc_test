if __name__ == '__main__':
    import grpc
    from dcs.mission.v0 import mission_pb2_grpc, mission_pb2

    print("hi")
    channel = grpc.insecure_channel('127.0.0.1:50051')
    stub = mission_pb2_grpc.MissionServiceStub(channel)

    events = stub.StreamEvents(mission_pb2.StreamEventsRequest())
    for event in events:
        print(event)

