import os
import sys
import json
import spotipy
import webbrowser
import spotipy.util as util
from json.decoder import JSONDecodeError
from track import Track
from jsonHandler import JsonHandler

scope = "user-modify-playback-state user-library-read playlist-read-private streaming user-read-recently-played"

# Get the username from terminal
username = sys.argv[1]

#User ID: 

#erase cache and promt for user permission

try:
    token = util.prompt_for_user_token(username, scope=scope)
except:
    os.remove(f".cache-{username}")
    token = util.prompt_for_user_token(username, scope=scope)

# Create our spotifyObject
spotifyObject = spotipy.Spotify(auth=token)

def getArtists(item):
    #item = items["items"][x]
    artist = item["track"]["artists"]
    for i in artist:
        print(f'Artist: {i["name"]}')

def getTitle(item):

    title = item["track"]["name"]
    print(f"Tittel: {title}")

def getLastPlayed(item):
    value = item["played_at"]
    print(type(value))



def getInfo(tracks):
    teller = 1
    for i in tracks["items"]:
        print(f"{teller}:")
        teller += 1
        getArtists(i)
        getTitle(i)
        getLastPlayed(i)
        print("-"*20)
        break
        


items = spotifyObject.current_user_recently_played(limit=50, before=None, after=None)
print("-"*50)
jsonHandlerLog = JsonHandler("listenLog.json")
jsonHandlerArtist = JsonHandler("artists.json")
jsonHandlerTracks = JsonHandler("tracks.json")




liste = []
for i in items["items"]:
    liste.append(Track(i))
test = 0
for i in liste:
    print("-"*20)
    test = i
    jsonHandlerLog.addRecord(test.toJson())

    
#print(test.getAlbumInfo())
#print(test.getArtistsInfo())
    print(test.getInfo())

#Print artists
#getArtists(items["items"][0])

#print title
#getTitle(items["items"][0])

#getInfo(items)
#Test

