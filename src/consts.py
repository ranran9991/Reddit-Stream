import os

# Kafka
KAFKA_BOOTSTRAP_SERVERS = ['localhost:9092']

# Reddit
CLIENT_ID = os.getenv('REDDIT_CLIENT_ID')
CLIENT_SECRET = os.getenv('REDDIT_CLIENT_SECRET')
USER_AGENT = 'python:stream:1.0'
SUBREDDIT = 'ani_bm'
