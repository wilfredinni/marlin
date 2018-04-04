import json
import os


class ManageBookmark:

    bookmark_path = os.path.join(
        os.path.dirname(__file__), 'bookmarks.json')

    def __init__(self, json_file):
        self.json_file = json_file

    def read_json(self):
        with open(self.json_file, 'r') as f:
            return json.load(f)

    def add_bookmark(self, content):
        with open(self.json_file, 'w') as f:
            json.dump(content, f)
