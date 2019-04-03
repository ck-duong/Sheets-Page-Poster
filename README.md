# Sheets-Page-Poster
A Python script that parses a Google spreadsheet and automatically posts numbered anonymous posts to a Facebook page. Requires Google Drive API and Facebook Graph API.

Install oauth2client (to authorize Google Drive API), gspreads (to interact with Google Sheets), facebook-sdk (to access Facebook/posting privileges)

pip install oauth2client
pip instsall gspreads
pip install facebook-sdk

For access to the Google Sheets spreadsheet:
1. Go to Google API Console (https://console.developers.google.com/)
2. Make/Access Google API Project
3. Enable Google Drive/Google Sheets API
4. Create credentials for a Web Server to access Application Data
5. Give service account the role of Project Editor or Owner
6. Download JSON key, copy to your code directory
7. Open client-secret.json, share editing access to the "client-email" in the file (should take the place of the provided credentials.json)
8. Paste spreadsheet name where indicated in confessions.py

To get Facebook user access key:
1. Go to Facebook for Developers (https://developers.facebook.com/)
2. Create an account/Login to account
3. Go to Graph API under Tools
4. Create an app
5. Grant manage_pages, publish_pages permissions
6. Get User/Page access tokens (depending on who you want to post as)
7. Enter token when running confessions.py
