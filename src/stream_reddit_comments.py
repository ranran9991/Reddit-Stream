import praw
import json
from kafka import KafkaProducer
from dotenv import load_dotenv
from consts import KAFKA_BOOTSTRAP_SERVERS, CLIENT_ID, CLIENT_SECRET, USER_AGENT, SUBREDDIT
from src.entities.comment import Comment

load_dotenv()

# Initialize Kafka Producer
producer = KafkaProducer(bootstrap_servers=KAFKA_BOOTSTRAP_SERVERS,
                         value_serializer=lambda x: json.dumps(x).encode('utf-8'))

# Initialize Reddit
reddit = praw.Reddit(client_id=CLIENT_ID,
                     client_secret=CLIENT_SECRET,
                     user_agent=USER_AGENT)

subreddit = reddit.subreddit(SUBREDDIT)

for comment_instance in subreddit.stream.comments():
    comment = Comment(str(comment_instance.author), comment_instance.created_utc, comment_instance.body,
                      comment_instance.submission_id, comment_instance.id)
    producer.send('comments', value=comment.to_protocolized_message().__dict__)
    print(f"Sent comment by {comment.author}")
