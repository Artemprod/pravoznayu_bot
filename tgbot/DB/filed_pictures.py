import os
import random

from tgbot.DB.db_interface import PictureRepo
from tgbot.enteties import Picture


class GetPictureFomFile(PictureRepo):

    def __init__(self, picture_dir):
        self.picture_dir = picture_dir
        self.file_paths = []

    def get_picture(self) -> Picture:
        if len(self.file_paths) == 0:
            self.get_all_file_paths()
        path = random.choice(self.file_paths)
        name = os.path.basename(path)
        return Picture(
            id=random.randint(100, 999),
            link_to_picture=path,
            article_name=name,
        )

    def get_all_file_paths(self):
        for root, dirs, files in os.walk(self.picture_dir):
            for file in files:
                self.file_paths.append(os.path.join(root, file))

    def save_new_picture(self):
        pass

    def delete_picture(self):
        pass
