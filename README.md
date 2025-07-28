# NIDS Backend (Flask + IBM Cloud)

This is a lightweight Flask backend to interact with your IBM Cloud-deployed NIDS ML model. Designed to be deployed on Render.com.

## Usage
POST JSON to `/predict` endpoint.

## Deployment (Render)
1. Push to GitHub
2. Go to https://render.com
3. Create new Web Service → Connect GitHub → Choose this repo
4. Set:
   - Runtime: Python
   - Start command: `gunicorn app:app`
   - Environment: `API_KEY`, `DEPLOYMENT_URL` (or hardcode in `app.py`)
