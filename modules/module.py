from abc import ABC, abstractmethod


class Module(ABC):

    def __init__(self, name, text):
        self.name = name
        self.text = text
        super().__init__()

        @abstractmethod
        def btn_clicked(self):
            pass
