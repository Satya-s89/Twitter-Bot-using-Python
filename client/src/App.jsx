import React, {useState} from "react";
import axios from "axios";
import "./App.css";

function App() {
  const [message, setMessage] = useState('');

  const postTweet = async () => {
    console.log("=== POST TWEET DEBUG ===");
    console.log("Message before sending:", message);
    console.log("Message length:", message.length);
    console.log("Message trimmed:", message.trim());
    console.log("Message trimmed length:", message.trim().length);
    
    if (!message.trim()) {
      console.log("Message is empty, showing alert");
      alert("Please enter a message");
      return;
    }
    
    const payload = {message};
    console.log("Payload being sent:", payload);
    console.log("Payload JSON:", JSON.stringify(payload));
    
    try {
      console.log("Sending request to Flask...");
      const apiUrl = import.meta.env.VITE_API_URL || "http://127.0.0.1:5000";
      const response = await axios.post(`${apiUrl}/api/tweet`, payload);
      console.log("Response received:", response);
      console.log("Response data:", response.data);
      console.log("Response status:", response.status);
      
      if (response.data.Success) {
        console.log("Tweet successful, clearing message");
        setMessage("");
        alert("Tweet posted!");
      } else {
        console.log("Tweet failed:", response.data.error);
        alert("Error: " + (response.data.error || "Failed to post"));
      }
    } catch (error) {
      console.error("Request failed:", error);
      console.error("Error response:", error.response);
      alert("Failed to post tweet");
    }
    
    console.log("=== END DEBUG ===");
  };

  return (
    <div className="container">
      <div className="card">
        <h1>🐦 Twitter Bot Dashboard</h1>
        <div className="tweet-form">
          <textarea
            className="tweet-input"
            value={message}
            onChange={(e) => {
              console.log("Message changed to:", e.target.value);
              setMessage(e.target.value);
            }}
            placeholder="What's happening?"
            maxLength="280"
          />
          <div className="form-footer">
            <span className="char-count">{message.length}/280</span>
            <button 
              className="tweet-btn" 
              onClick={postTweet} 
              disabled={!message.trim()}
            >
              Tweet
            </button>
          </div>
        </div>
      </div>
    </div>
  )
}

export default App;
