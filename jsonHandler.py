import json

class JsonHandler:
    def __init__(self, filename):
        self.filename = filename

    #Adding records to dict ready to be written to .json
    def addRecord(self, record):
        data = self.readFile()

        key = list(record.keys())[0]
        if key not in data.keys():
            data.update(record)

        #print(record.keys())

        self.writeFile(data)
    
    def readRecord(self, id):
        pass

    def add(self, records):
        data = self.readFile()
        for record in records:
            key = list(record.keys())[0]
            if key not in data.keys():
                data.update(record)
            
        self.writeFile(data)

    def readFile(self):
        with open(self.filename) as json_file:
            return json.load(json_file)

    #Data er HELE inholdet i filen
    def writeFile(self, data):
        with open(self.filename, "w") as f:
            json.dump(data, f, indent=4)

    