import time
import json
from concurrent import futures

import grpc
import location_grpc_pb2
import location_grpc_pb2_grpc

from app.udaconnect.models import Location

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import os

from sqlalchemy.ext.declarative import declarative_base
from kafka import KafkaProducer


class LocationServicer(location_grpc_pb2_grpc.LocationServiceServicer):
    def __init__(self) -> None:
        DB_USERNAME = os.environ["DB_USERNAME"]
        DB_PASSWORD = os.environ["DB_PASSWORD"]
        DB_HOST = os.environ["DB_HOST"]
        DB_PORT = os.environ["DB_PORT"]
        DB_NAME = os.environ["DB_NAME"]

        engine = create_engine(
            f"postgresql://{DB_USERNAME}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}")
        SessionClass = sessionmaker(engine)
        self.session = SessionClass()

        self.TOPIC_NAME = os.environ['KAFKA_TOPIC']
        KAFKA_SERVER = os.environ['KAFKA_SERVER']
        self.producer = KafkaProducer(bootstrap_servers=KAFKA_SERVER)

    def Create(self, request, context):

        request_value = {
            "longitude": request.longitude,
            "person_id": int(request.person_id),
            "latitude": request.latitude,
        }
        kafka_data = json.dumps(request_value).encode()
        print(self.TOPIC_NAME, kafka_data)
        self.producer.send(self.TOPIC_NAME, kafka_data)

        return location_grpc_pb2.LocationMessage(**request_value)


# Initialize gRPC server
server = grpc.server(futures.ThreadPoolExecutor(max_workers=2))
location_grpc_pb2_grpc.add_LocationServiceServicer_to_server(
    LocationServicer(), server)


print("Server starting on port 5005...")
server.add_insecure_port("[::]:5005")
server.start()
# Keep thread alive
try:
    while True:
        time.sleep(86400)
except KeyboardInterrupt:
    server.stop(0)