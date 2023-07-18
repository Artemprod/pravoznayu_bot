from abc import ABC, abstractmethod


class DataBaseConnection(ABC):
    pass


class DataBase(ABC):

    @abstractmethod
    def read(self):
        pass

    @abstractmethod
    def create(self):
        pass

    @abstractmethod
    def delete(self):
        pass

    @abstractmethod
    def update(self):
        pass

class UserRepo(ABC):

    @abstractmethod
    def get_user(self):
        pass

    @abstractmethod
    def create_user(self):
        pass

    @abstractmethod
    def check_user(self):
        pass

    @abstractmethod
    def delete_user(self):
        pass


class PictureRepo(ABC):

    @abstractmethod
    def get_picture(self):
        pass

    @abstractmethod
    def save_new_picture(self):
        pass

    @abstractmethod
    def delete_picture(self):
        pass

