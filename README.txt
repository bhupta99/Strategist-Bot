Strategist Bot Setup Guide
==========================

Step 1: Upload Files to GitHub
------------------------------
1. Go to your GitHub repository
2. Click "Add file" → "Create new file"
3. Create and commit the following files:
   - app.py
   - requirements.txt
   - Procfile

Step 2: Deploy to Render
------------------------
1. Go to https://render.com
2. Create a new Web Service
3. Connect your GitHub repo
4. Set the build and start commands:
   - Build command: pip install -r requirements.txt
   - Start command: python app.py
5. Choose a free plan and deploy

Step 3: Set Telegram Webhook
----------------------------
1. Replace 'YOUR_BOT_TOKEN_HERE' in app.py
