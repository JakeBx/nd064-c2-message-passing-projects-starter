import grpc
import location_grpc_pb2
import location_grpc_pb2_grpc

"""
Sample implementation of a writer that can be used to write messages to gRPC.
"""

print("Sending sample payload...")

channel = grpc.insecure_channel("localhost:30004")
stub = location_grpc_pb2_grpc.LocationServiceStub(channel)

# Update this with desired payload
location = location_grpc_pb2.LocationMessage(
    longitude="37.553442",
    person_id=7,
    latitude="-122.290524",
)


response = stub.Create(location)
print(response)