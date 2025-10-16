import random

TWEET_MESSAGES = [
    "Good morning!",
    "Have a great day!",
    "Stay posistive"
]

HASHTAGS = ["#python", "#bot", "#automation"]

TWEET_TEMPLATES = [
    "Good morning! Today is {day}",
    "Motivation Monday: {quote}",
    "Tech tip: {tip}"
]

def generate_content():
    return random.choice(TWEET_TEMPLATES)

