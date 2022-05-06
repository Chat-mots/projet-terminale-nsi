from obstacle import Obstacle

class Printer(Obstacle):
    def __init__(self, mot):
        self.mot = mot

    def afficage(self):
        print(self.mot)
