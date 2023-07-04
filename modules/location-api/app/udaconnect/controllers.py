from datetime import datetime
import json

from app.udaconnect.models import Connection, Location, Person
from app.udaconnect.schemas import (
    ConnectionSchema,
    LocationSchema,
    PersonSchema,
)
from app.udaconnect.services import LocationService, PersonService
from flask import request, jsonify
from flask_accepts import accepts, responds
from flask_restx import Namespace, Resource
from typing import Optional, List

from kafka import KafkaProducer

DATE_FORMAT = "%Y-%m-%d"

api = Namespace("UdaConnect", description="Connections via geolocation.")  # noqa


TOPIC_NAME = 'location-events'
KAFKA_SERVER = 'localhost:9092'

producer = KafkaProducer(bootstrap_servers=KAFKA_SERVER)


@api.route("/locations")
@api.route("/locations/<location_id>")
@api.param("location_id", "Unique ID for a given Location", _in="query")
class LocationResource(Resource):
    @accepts(schema=LocationSchema)
    @responds(schema=LocationSchema)
    def post(self) -> Location:
        payload = json.dumps(request.get_json()).encode('utf-8')
        producer.send(TOPIC_NAME, payload)
        producer.flush()

        response = jsonify({"result": True})
        return response


    @responds(schema=LocationSchema)
    def get(self, location_id) -> Location:
        location: Location = LocationService.retrieve(location_id)
        return location

