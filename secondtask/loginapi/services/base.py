from abc import ABC, abstractmethod

class baseClass(ABC):
    @abstractmethod
    def validationForEmail(self):
        pass
    @abstractmethod
    def validationForPhone(self):
        pass
   