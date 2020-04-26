# imports
import spotipy
import spotipy.util as util
from spotipy.oauth2 import SpotifyClientCredentials
import os
import sys
import json
import requests
import pandas as pd

'''
Goal is to make some sort of tool using
Spotify API

- get music preferences and present data using plotly?
- recommend songs
- convert youtube playlist to spotify
'''

# Relearning Python OOP
class User:
    name = str()

    # util.prompt_for_user_token(username,
    #                        scope,
    #                        client_id='your-spotify-client-id',
    #                        client_secret='your-spotify-client-secret',
    #                        redirect_uri='your-app-redirect-url')



# get authorization for user account
def get_auth(self, username):
    scope = 'user-library-read'
    token = util.prompt_for_user_token(username, scope)

    if token:
        sp = spotipy.Spotify(auth=token)
        results = sp.current_user_saved_tracks()
        for item in results['items']:
            track = item['track']
            print(track['name'] + ' - ' + track['artists'][0]['name'])
        return True
    else:
        print("Can't get token for", username)
        return False


def get_user(self, *args):
    return self.name[0], args


# retrieve songs from user accnt as dataframe
def get_songs():
    pass

# def print_user(User)

# create user
user = User()
user.name = "Ronnie"
print(user.name)
# print(get_user(user, "Test", "Test1"))
# print(os.getcwd())

username = input("What is your Spotify name?\n")
print(f"Username: {username}")



# response = requests.get("https://api.spotify.com/v1/")
# print(response.json)
# sp = spotipy.Spotify(client_credentials_manager=SpotifyClientCredentials())


df = pd.DataFrame()
print(df)