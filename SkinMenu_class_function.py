# lavet af Hveppe

import pygame
from objekts import Button, Picture
from Define import Grey, Red, Orange
from Sidefunctions import tint_image
from Sidefunctions import tekst_render

pygame.font.init()
Font = pygame.font.SysFont('Comic Sans MS', 36, bold=False, italic=False)


class SkinSlecter:
    def __init__(self, screen, x, y, size, type_skin,  *args):
        self.screen = screen
        self.x = x
        self.y = y
        self.width, self.height = size
        self.chosenskin = 0

        self.type = type_skin

        if self.type == "player":
            self.skins = [*args]
        elif self.type == "cursor":
            rangeskin = [*args]
            self.skins = rangeskin[0::2]
            self.skinsclick = rangeskin[1::2]

        self.RightButton = Button(self.screen, "", (50, 100), pygame.transform.scale(pygame.image.load(
            "Image/Buttons/Arrow_button.png"), (50, 100)))
        self.LeftButton = Button(self.screen, "",
                                 (50, 100), pygame.transform.rotate(pygame.transform.scale(
                                      pygame.image.load("Image/Buttons/Arrow_button.png"), (50, 100)), 180))

    def buttondraw(self):
        if self.RightButton.draw(self.x+self.width-(10+self.RightButton.width),
                                 self.y+self.height/2-self.RightButton.height/2) is True:
            if self.chosenskin < len(self.skins)-1:
                self.chosenskin += 1
            else:
                self.chosenskin = 0

            if self.type == "player":
                return self.skins[self.chosenskin], tint_image(self.skins[self.chosenskin], Red)
            elif self.type == "cursor":
                return self.skins[self.chosenskin], self.skinsclick[self.chosenskin]

        if self.LeftButton.draw(self.x+10, self.y+self.height/2-self.LeftButton.height/2) is True:
            if self.chosenskin > 0:
                self.chosenskin -= 1
            else:
                self.chosenskin = len(self.skins)-1

            if self.type == "player":
                return self.skins[self.chosenskin], tint_image(self.skins[self.chosenskin], Red)
            elif self.type == "cursor":
                return self.skins[self.chosenskin], self.skinsclick[self.chosenskin]

    def draw(self, tekst):
        skinpicture = Picture(self.screen, self.x+self.width/2-50, self.y+self.height/2-50,
                              pygame.transform.scale(self.skins[self.chosenskin], (100, 100)))

        pygame.draw.rect(self.screen, Grey, (self.x, self.y, self.width, self.height))
        skinpicture.draw()

        tekst_render(Font, tekst, (self.x+self.width/2, self.y-5), self.screen, Orange, True)

    def change_skin(self):
        while True:
            if self.type == "player":
                return self.skins[self.chosenskin], tint_image(self.skins[self.chosenskin], Red)
            elif self.type == "cursor":
                return self.skins[self.chosenskin], self.skinsclick[self.chosenskin]
