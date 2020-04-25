# imports
import os
import json
import requests
import spotipy

'''
Goal is to make some sort of tool using
Spotify API
'''

# Relearning Python OOP
class User:
    name = "Name"


def get_user(self, *args):
    return self.name[0], args

# def print_user(User)

user = User()
print(user.name)
print(get_user(user, "Test", "Test1"))
print(os.getcwd())

response = requests.get("https://api.spotify.com/v1/")
print(response.json)
