import praw
from dotenv import load_dotenv
from consts import CLIENT_ID, CLIENT_SECRET, USER_AGENT, SUBREDDIT
from src.entities.post import Post
from kafka import KafkaProducer

load_dotenv()
# # Initialize Kafka Producer
producer = KafkaProducer(bootstrap_servers=KAFKA_BOOTSTRAP_SERVERS,
                         value_serializer=lambda x: json.dumps(x).encode('utf-8'))

# Initialize Reddit
reddit = praw.Reddit(client_id=CLIENT_ID,
                     client_secret=CLIENT_SECRET,
                     user_agent=USER_AGENT)

subreddit = reddit.subreddit(SUBREDDIT)

# Stream posts and send to Kafka
for submission in subreddit.stream.submissions():
    post = Post(submission.id, submission.title, submission.selftext, str(submission.author), submission.created_utc,
                submission.url)
    producer.send('posts', value=post.to_protocolized_message().__dict__)
    print(f"Sent post: {submission.title}")
