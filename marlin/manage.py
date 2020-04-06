import os
from pathlib import Path


class ManageBookmark:
    marlin_path = Path((Path.home()) / ".marlin")

    def __init__(self, bookmark_name, bookmark_path, m_path=marlin_path):
        self.bookmark_name = bookmark_name
        self.bookmark_path = bookmark_path
        self.m_path = m_path

    def add_bookmark(self):
        os.chdir(self.m_path)
        with open(self.bookmark_name, "w", encoding="utf-8") as f:
            f.write(self.bookmark_path)

    def remove_bookmark(self):
        os.chdir(self.m_path)
        os.unlink(self.bookmark_name)

    def list_bookmark(self):
        return os.listdir(self.m_path)

    def read_bookmark(self, bookmark):
        os.chdir(self.m_path)
        with open(bookmark, "r", encoding="utf-8") as f:
            return f.read()

    def create_marlin_folder(self):
        exists = Path(self.m_path).exists()
        if not exists:
            (self.m_path).mkdir()
