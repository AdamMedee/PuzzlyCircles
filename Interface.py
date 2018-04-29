from pygame import *
from math import *
from random import *

init()


class Button:
    def __init__(self, rect, image, imageP, name):
        self.rect = rect
        self.image = transform.scale(image, (rect[2], rect[3]))
        self.imageP = transform.scale(imageP, (rect[2], rect[3]))
        self.name = name

    def mouseOver(self, mouseCoords):
        return self.rect.collidepoint(mouseCoords)

    def clicked(self, mouseCoords, mouseClicked):
        return mouseClicked and self.mouseOver(mouseCoords)

    def getName(self):
        return self.name

    def update(self, screen, mouseCoords):
        if self.mouseOver(mouseCoords):
            screen.blit(self.imageP, self.rect)
        else:
            screen.blit(self.image, self.rect)
