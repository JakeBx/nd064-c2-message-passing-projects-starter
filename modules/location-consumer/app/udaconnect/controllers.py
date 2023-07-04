from datetime import datetime

from app.udaconnect.models import Connection, Location, Person
from app.udaconnect.schemas import (
    ConnectionSchema,
    LocationSchema,
    PersonSchema,
)
from app.udaconnect.services import LocationService, PersonService
from flask import request
from flask_accepts import accepts, responds
from flask_restx import Namespace, Resource
from typing import Optional, List
from kafka import KafkaConsumer

DATE_FORMAT = "%Y-%m-%d"
TOPIC_NAME = 'location-events'
KAFKA_SERVER = 'localhost:9092'
consumer = KafkaConsumer(TOPIC_NAME)

while True:
    for message in consumer:
        print(message)

# api = Namespace("UdaConnect", description="Connections via geolocation.")  # noqa
#
#
# # TODO: This needs better exception handling
#
#
# @api.route("/locations")
# @api.route("/locations/<location_id>")
# @api.param("location_id", "Unique ID for a given Location", _in="query")
# class LocationResource(Resource):
#     @accepts(schema=LocationSchema)
#     @responds(schema=LocationSchema)
#     def post(self) -> Location:
#         # request.get_json()
#         while True:
#         # location: Location = LocationService.create(request.get_json())
#         # return location

