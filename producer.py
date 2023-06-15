from kafka import KafkaProducer
import json
from dotenv import load_dotenv
import os
# Load variables from .env file
load_dotenv('.env')

# Access the variables
pw = os.getenv('upstashpw')
 




producer = KafkaProducer(
  bootstrap_servers=['equal-owl-9135-us1-kafka.upstash.io:9092'],
  sasl_mechanism='SCRAM-SHA-256',
  security_protocol='SASL_SSL',
  sasl_plain_username='ZXF1YWwtb3dsLTkxMzUkXx5J8vYxwycFJ6cLxNilKEWjb-e9US4xNfsLc0abcOo',
  sasl_plain_password= pw
  value_serializer=lambda v: json.dumps(v).encode('utf-8'),
)





message = {'test' : 'test1'}

producer.send()



producer.close()