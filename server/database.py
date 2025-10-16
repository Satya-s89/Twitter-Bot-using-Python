import sqlite3

def init_db():
    conn = sqlite3.connect('bot.db')
    conn.execute('''CREATE TABLE IF NOT EXISTS tweets
                 (id INTEGER PRIMARY KEY, message TEXT, timestamp DATETIME)''')
    conn.close()

def save_tweet(message):
    conn = sqlite3.connect('bot.db')
    conn.execute("INSERT INTO tweets (message, timestamp) VALUES (?, datetime('now'))", (message,))
    conn.commit()
    conn.close()

def get_tweet_history():
    conn = sqlite3.connect('bot.db')
    cursor = conn.execute("SELECT * FROM tweets ORDER BY timestamp DESC LIMIT 10")
    tweets = cursor.fetchall()
    conn.close()
    return tweets
