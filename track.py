import datetime
import json

class Track:
    def __init__(self, track):
        self.track = track


    def getTitle(self):
        title = self.track["track"]["name"]
        return title

    def getArtistList(self):
        liste = []
        artist = self.track["track"]["artists"]
        for i in artist:
            liste.append(i["name"])
        return liste


    def getArtists(self):
        artist = self.track["track"]["artists"]
        string = ""
        for i in artist:
            #print(f'Artist: {i["name"]}')
            string += f"{i['name']}, "

        return string[:-2]

    def getMs(self):
        return int(self.getLastPlayed().timestamp() * 1000)
        


    def getLastPlayed(self):
        value = self.track["played_at"]
        dateTime = datetime.datetime.fromisoformat(value[:-1])
        return dateTime

    def getTrackId(self):
        value = self.track["track"]["id"]
        return value

    def isExplicit(self):
        return self.track["track"]["explicit"]


    def getKeys(self):
        print(self.track.keys())

    def getInfo(self):
        string = ""
        string += f"Artist: {self.getArtists()}"
        string += f"\nTitle: {self.getTitle()}"
        string += f"\nLast played: {self.getLastPlayed().strftime('%d.%m.%Y %H:%M:%S')}"
        string += f"\nMs: {self.getMs()}"


        return string

    def getTrackInfo(self):

        #string = ""

        #string += f"\nId: {self.track['track']['id']}"
        #string += f"\nName: {self.track['track']['name']}"

        track = self.track["track"]
        track["available_markets"] = ""
        track["album"]["available_markets"] = ""
        
        return self.makePritty(track)

    def getArtistsInfo(self):
        string = "Artists:"
        for artist in self.track['track']['artists']:
        
            string += f"\n\tId: {artist['id']}"
            string += f"\n\tName: {artist['name']}"
            string += "\n"

        return string

    def getListenLogInfo(self):
        pass

    def getAlbumInfo(self):
        
        track = self.track["track"]["album"]
        keys = list(track.keys())
        keys.remove("available_markets")
        keys.remove("id")
        
        content = {}
        for key in keys:
            content[key] = track[key]
        album = {track["id"]: content}

        return self.makePritty(album)


    def __str__(self):

        #string = ""
        #string += f"{self.track['track'].keys()}"
        
        #string += "track"
        #for key in self.track["track"].keys():
        #    string += f"\n\t{key}"

        #string += "\ncontext"
        #for key in self.track["context"].keys():
        #    string += f"\n\t{key}"

        #string += f"\n{self.track['played_at']}"
        #string += f"\n{self.track['context'].keys()}"

        return self.makePritty(self.track["track"])

    def toJson(self):
        return {
            self.getMs(): {
                "artist": self.getArtistList(),
                "title": self.getTitle(),
                "played": self.getLastPlayed().strftime('%d.%m.%Y %H:%M:%S')
            }
        }
    
    def makePritty(self, dict):
        return json.dumps(dict, indent=4)