import json
import os


class ManageBookmark:

    bookmark_path = os.path.join(
        os.path.dirname(__file__), 'bookmarks.json')

    def __init__(self, json_file):
        self.json_file = json_file
