from jsonHandler import JsonHandler
#Handelig all json distrinution about tracks, artist and instances

FILENAMES = ("artist.json", "tracks.json", "listenLog.json")

class Handler:
    def __init__(self):
        self.artistHandler = JsonHandler(FILENAMES[0])
        self.trackHandler = JsonHandler(FILENAMES[1])
        self.listenLogHandler = JsonHandler(FILENAMES[2])

    
    def addTrack(self, track):
        pass
