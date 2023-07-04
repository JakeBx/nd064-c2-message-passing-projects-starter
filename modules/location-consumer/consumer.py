# from typing import Dict
# from concurrent import futures

# from app.udaconnect.models import Location

from sqlalchemy import create_engine
# from sqlalchemy.orm import sessionmaker
import os
import json

# from sqlalchemy.ext.declarative import declarative_base
from kafka import KafkaConsumer
#
# from geoalchemy2.functions import ST_Point
# from app.udaconnect.models import Location
# from app.udaconnect.schemas import LocationSchema

DB_USERNAME = os.environ["DB_USERNAME"]
DB_PASSWORD = os.environ["DB_PASSWORD"]
DB_HOST = os.environ["DB_HOST"]
DB_PORT = os.environ["DB_PORT"]
DB_NAME = os.environ["DB_NAME"]

SQLALCHEMY_DATABASE_URI = f"postgresql://{DB_USERNAME}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"

engine = create_engine(SQLALCHEMY_DATABASE_URI)
conn = engine.connect()

# DATE_FORMAT = "%Y-%m-%d"
TOPIC_NAME = 'location-events'
KAFKA_SERVER = 'localhost:9092'
consumer = KafkaConsumer(TOPIC_NAME, api_version=(3,5,0))


while True:
    for message in consumer:
        payload = json.loads(message.value)
        person_id = payload["person_id"]
        latitude = payload["latitude"]
        longitude = payload["longitude"]
        insert = "INSERT INTO location (person_id, coordinate) VALUES ({}, ST_Point({}, {}))" \
            .format(person_id, latitude, longitude)

        print(insert)
        conn.execute(insert)

        print(payload)
