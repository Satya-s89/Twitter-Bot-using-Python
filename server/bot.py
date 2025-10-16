import tweepy
import os
from dotenv import load_dotenv
import schedule
import time
import logging
from config import generate_content, TWEET_MESSAGES
import random
from database import init_db, save_tweet

load_dotenv()
init_db()

api_key = os.getenv("API_KEY")
api_secret = os.getenv("API_SECRET_KEY")
access_token = os.getenv("ACCESS_TOKEN")
access_token_secret = os.getenv("ACCESS_TOKEN_SECRET")
bearer_token = os.getenv("BEARER_TOKEN")


logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

client = tweepy.Client(bearer_token=bearer_token, consumer_key=api_key, consumer_secret=api_secret, access_token=access_token, access_token_secret=access_token_secret)

def post_tweet(message):
    try:
        responce = client.create_tweet(text = message)
        save_tweet(message)
        print(f"Tweet posted: {responce.data['id']}")
        return True
    except Exception as e:
        print(f"Error: {e}")
        return False

def post_random_tweet():
    message = random.choice(TWEET_MESSAGES)
    post_tweet(message)  
  
def scheduled_tweet():
    post_tweet("Daily automated tweet!")

def start_scheduler():
    schedule.every().day.at("09:00").do(scheduled_tweet)
    
    while True:
        schedule.run_pending()
        time.sleep(60)


def get_mentions():
    mentions = client.get_mentions(tweet_fields=['author_id','text'])
    return mentions.data if mentions.data else []

def reply_to_tweet(tweet_id, message):
    client.create_tweet(text = message, in_reply_to_tweet_id = tweet_id)

def like_tweet(tweet_id):
    client.like(tweet_id)

def follow_user(user_id):
    client.follow_user(user_id)

def auto_reply_mentions():
    mentions = get_mentions()
    for mention in mentions:
        reply_to_tweet(mention.id, "Thanks for mentioning me")
    
if __name__ == "__main__":
    print("1. Post single tweet")
    print("2. Start scheduled tweets")
    print("3. Check mentions")

    choice = input("Choose option: ")

    if choice == "1":
        message = input("Enter tweet: ")
        post_tweet(message)
    elif choice == '2':
        start_scheduler()
    elif choice == "3":
        mentions = get_mentions()
        for mention in mentions:
            print(f"@{mention.author_id} : {mention.text}")