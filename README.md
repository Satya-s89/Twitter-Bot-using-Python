# Twitter Bot with React Frontend

A full-stack Twitter bot application with a React frontend and Flask backend.

## Features
- Post tweets through web interface
- Real-time tweet posting
- Character count validation
- Responsive design

## Tech Stack
- **Frontend:** React + Vite
- **Backend:** Flask + Python
- **API:** Twitter API v2
- **Database:** SQLite

## Setup

### Backend
```bash
cd server
pip install -r requirements.txt
cp .env.example .env  # Add your Twitter API credentials
python app.py
```

### Frontend
```bash
cd client
npm install
npm run dev
```

## Environment Variables
Add these to `server/.env`:
```
API_KEY=your_twitter_api_key
API_SECRET_KEY=your_twitter_api_secret
BEARER_TOKEN=your_twitter_bearer_token
ACCESS_TOKEN=your_twitter_access_token
ACCESS_TOKEN_SECRET=your_twitter_access_token_secret
CLIENT_ID=your_twitter_client_id
CLIENT_SECRET=your_twitter_client_secret
```

## Deployment
See [DEPLOYMENT.md](DEPLOYMENT.md) for Netlify and Render deployment instructions.
