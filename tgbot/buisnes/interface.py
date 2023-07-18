from abc import ABC, abstractmethod


class GetConstitutionKnowledges(ABC):

    @abstractmethod
    def send_knowledge(self):
        pass

    @abstractmethod
    def set_frequency(self):
        pass
