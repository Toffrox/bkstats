class DiscordStats:
    def __init__(self):
        self.data = {}

    def getCount(self, uid):
        try:
            return self.data[uid]
        except KeyError:
            return 0

    def increment(self, uid):
        try:
            self.data[uid] += 1
        except KeyError:
            self.data[uid] = 1
    
    def clear(self):
        self.data.clear()

