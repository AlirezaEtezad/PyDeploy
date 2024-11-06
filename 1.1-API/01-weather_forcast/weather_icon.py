import random
import arcade

class Icon(arcade.Sprite):
        def __init__(self):
            super().__init__()
            self.width = 200
            self.height = 100
            self.center_x = 200
            self.center_y = 250



class Sunny(Icon):
    def __init__(self):
        super().__init__()
        self.texture = arcade.load_texture("sunny.png")
        self.width = 250
        self.height = 150



class Cloudy(Icon):
    def __init__(self):
        super().__init__()
        self.texture = arcade.load_texture("cloudy.png")
        self.width = 250
        self.height = 150


class Rainy(Icon):
    def __init__(self):
        super().__init__()
        self.texture = arcade.load_texture("rainy.png")
        self.width = 250
        self.height = 150

class Snowy(Icon):
    def __init__(self):
        super().__init__()
        self.texture = arcade.load_texture("snowy.png")
        self.width = 250
        self.height = 150