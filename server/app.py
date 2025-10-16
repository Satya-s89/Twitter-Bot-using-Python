import os
from flask import Flask, render_template, request, jsonify
from flask_cors import CORS
from bot import post_tweet, get_mentions

app = Flask(__name__)

# Configure CORS for both development and production
allowed_origins = [
    "http://localhost:5173",
    "http://127.0.0.1:5173"
]

# Add production frontend URL if provided
if os.getenv('FRONTEND_URL'):
    allowed_origins.append(os.getenv('FRONTEND_URL'))

CORS(app, origins=allowed_origins)

@app.route("/api/tweet", methods=["POST"])
def tweet():
    try:
        print("=== FLASK DEBUG ===")
        print("Request received")
        data = request.get_json()
        print("Data received:", data)
        
        if not data or 'message' not in data:
            print("No message in data")
            return jsonify({"Success": False, "error": "No message provided"})
        
        message = data['message']
        print("Message:", repr(message))
        
        if not message.strip():
            print("Empty message")
            return jsonify({"Success": False, "error": "Message cannot be empty"})
        
        print("Calling post_tweet...")
        result = post_tweet(message)
        print("post_tweet result:", result)
        
        return jsonify({"Success": result})
        
    except Exception as e:
        print("Flask error:", str(e))
        return jsonify({"Success": False, "error": str(e)})

@app.route("/api/mentions", methods=["GET"])
def mentions():
    mentions = get_mentions()
    return jsonify({"mentions": mentions})

if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=False)
