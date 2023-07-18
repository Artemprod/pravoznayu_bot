from tgbot.DB.filed_pictures import GetPictureFomFile
from tgbot.buisnes.interface import GetConstitutionKnowledges
from tgbot.DB.db_interface import PictureRepo
from tgbot.enteties import User


class GetKnowledgeFromPicture(GetConstitutionKnowledges):

    def __init__(self, picture_repo: PictureRepo):
        self.picture_repo = picture_repo

    def send_knowledge(self):
        pic = self.picture_repo.get_picture()
        return pic.link_to_picture


    def set_frequency(self):
        pass

if __name__ == '__main__':
    a = GetKnowledgeFromPicture(picture_repo=GetPictureFomFile(picture_dir=r'D:\python projects\non_comertial\constitution\pictures'))
    link = a.send_knowledge()
    print()
