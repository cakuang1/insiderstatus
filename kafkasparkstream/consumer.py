from kafka import KafkaConsumer
import streamlit as st
import psycopg2
import pandas as pd
import os
from dotenv import load_dotenv
load_dotenv('.env')




un = os.getenv('upstashuser')
pw = os.getenv('upstashpw')








consumer = KafkaConsumer(
  bootstrap_servers=['equal-owl-9135-us1-kafka.upstash.io:9092'],
  sasl_mechanism='SCRAM-SHA-256',
  security_protocol='SASL_SSL',
  sasl_plain_username=un,
  sasl_plain_password=pw,
  group_id='$GROUP_NAME',
  auto_offset_reset='earliest',
)



























consumer.close()