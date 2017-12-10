import json

class Song:
    def __init__(self, filename):
        first = filename[2]
        second = filename[3]
        third = filename[4]
        if (first not in ['A', 'B']) or (first is 'B' and second not in ['A','B','C','D','E','F','G','H','I']):
            self.artist = "file"
            self.title = "not found"
            self.timestamp = "-1"
            self.track_id = filename
            self.tags = []
            self.similars = []
        else:
            json_name = "lastfm_subset/" + first + "/" + second + "/" + third + "/" + filename + ".json"
            f = open(json_name, "r")
            song_info = json.load(f)
            self.artist = song_info['artist']
            self.title = song_info['title']
            self.timestamp = song_info['timestamp']
            self.track_id = song_info['track_id']
            self.tags = song_info['tags']
            self.similars = song_info['similars']

    def get_tags(self, limit=None):
        if limit is None:
            result = []
            for tag in self.tags:
                result.append(tag[0])
            return result
        else:
            result = []
            for tag in self.tags:
                if int(tag[1]) >= limit:
                    result.append(tag[0])
            return result

    def get_similars(self, limit=None):
        if limit is None:
            result = []
            for similar in self.similars:
                result.append(similar[0])
            return result
        else:
            result = []
            for similar in self.similars:
                if similar[1] >= limit:
                    result.append(similar[0])
            return result

    def shared_tags(self, other_song_instance):
        result = []
        for tag in self.get_tags():
            if tag in other_song_instance.get_tags():
                result.append(tag)
        return tuple(result)

    def combined_tags(self, other_song_instance):
        result = set()
        for tag in self.get_tags():
            result.add(tag)
        for tag in other_song_instance.get_tags():
            result.add(tag)
        return tuple(result)


