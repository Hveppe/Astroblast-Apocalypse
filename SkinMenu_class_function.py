# lavet af Hveppe

import pygame
from objekts import Button, Picture
from Define import scalar, Grey, Red, Orange, Green, Yellow, Blue, DarkBlue, Purple, Pink, Cyan, Magenta
from Sidefunctions import tint_image
from Sidefunctions import tekst_render

pygame.font.init()


class SkinSlecter:
    Font = pygame.font.SysFont('Comic Sans MS', int(round(36*scalar.scalar, 0)), bold=False, italic=False)

    def __init__(self, screen, x, y, size, type_skin,  *args):
        self.screen = screen
        self.orginal_x, self.orginal_y = x, y
        self.x, self.y = x*scalar.scalar, y*scalar.scalar
        self.orginal_width, self.orginal_height = size
        self.width, self.height = self.orginal_width*scalar.scalar, self.orginal_height*scalar.scalar
        self.chosenskin = 0

        self.type = type_skin
        self.image = pygame.image.load("Image/Buttons/Arrow_button.png")

        if self.type == "player":
            self.skins = [*args]
        elif self.type == "cursor":
            rangeskin = [*args]
            self.skins = rangeskin[0::2]
            self.skinsclick = rangeskin[1::2]

        self.skinpicture = Picture(self.screen, self.x + self.width / 2 - 50, self.y + self.height / 2 - 50,
                                   pygame.transform.scale(self.skins[self.chosenskin], (100, 100)))

        self.RightButton = Button(self.screen, "", (50, 100),
                                  pygame.transform.scale(self.image, (50*scalar.scalar, 100*scalar.scalar)))
        self.LeftButton = Button(self.screen, "",
                                 (50, 100), pygame.transform.rotate(pygame.transform.scale(self.image,
                                                                                           (50*scalar.scalar,
                                                                                            100*scalar.scalar)), 180))

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
        self.skinpicture = Picture(self.screen, self.x+self.width/2-50*scalar.scalar, self.y+self.height/2-50*scalar.scalar,
                                   pygame.transform.scale(self.skins[self.chosenskin], (100*scalar.scalar, 100*scalar.scalar)))

        pygame.draw.rect(self.screen, Grey, (self.x, self.y, self.width, self.height))
        self.skinpicture.draw()

        tekst_render(self.Font, tekst, (self.x+self.width/2, self.y-5), self.screen, Orange, True)

    def change_skin(self):
        while True:
            if self.type == "player":
                return self.skins[self.chosenskin], tint_image(self.skins[self.chosenskin], Red)
            elif self.type == "cursor":
                return self.skins[self.chosenskin], self.skinsclick[self.chosenskin]

    def transform(self):  # Transformer størrelse så den passer med scalar
        self.x, self.y = self.orginal_x*scalar.scalar, self.orginal_y*scalar.scalar
        self.width, self.height = self.orginal_width*scalar.scalar, self.orginal_height*scalar.scalar
        self.Font = pygame.font.SysFont('Comic Sans MS', int(round(36*scalar.scalar, 0)), bold=False, italic=False)

        self.RightButton.image = self.image
        self.LeftButton.image = pygame.transform.rotate(self.image, 180)
        self.RightButton.transform(), self.LeftButton.transform()


class LaserColorChange:
    clicksound = pygame.mixer.Sound("sound/click-menu-app-147357.wav")
    Font = pygame.font.SysFont('Comic Sans MS', int(round(36 * scalar.scalar, 0)), bold=False, italic=False)

    def __init__(self, screen, destination, size):
        self.screen = screen
        self.orginal_x, self.orginal_y = destination
        self.x, self.y = self.orginal_x*scalar.scalar, self.orginal_y*scalar.scalar
        self.orginal_width, self.orginal_height = size
        self.width, self.height = self.orginal_width*scalar.scalar, self.orginal_height*scalar.scalar

        self.margin = 5
        self.square_size = 50*scalar.scalar
        self.gridsize = 5

        self.colors = [Red, Orange, Green, Yellow, Blue, Purple, Pink, Cyan, Orange, Magenta]

    def draw_color_grid(self):
        # udregner den totale størelse
        total_width = (self.gridsize * self.square_size) + ((self.gridsize - 1) * self.margin)
        total_height = (((len(self.colors) + self.gridsize - 1) // self.gridsize) * self.square_size) + (
                    ((len(self.colors) + self.gridsize - 1) // self.gridsize - 1) * self.margin)

        # tegner baggrund
        pygame.draw.rect(self.screen, Grey, (self.x-10*scalar.scalar, self.y-40*scalar.scalar, total_width+20*scalar.scalar, total_height+50*scalar.scalar))
        tekst_render(self.Font, "LASER COLOR", (self.x+total_width/2, self.y-50*scalar.scalar), self.screen, Orange, True)

        # tegner de andre color firekanter
        for index, color in enumerate(self.colors):
            x = (index % self.gridsize) * (self.square_size + self.margin) + self.x
            y = (index // self.gridsize) * (self.square_size + self.margin) + self.y
            pygame.draw.rect(self.screen, color, (x, y, self.square_size, self.square_size))

    def get_color_of_postion(self, pos, currentcolor):
        if self.collidemouse(pos):
            self.clicksound.play()
            x, y = pos
            col = int((x - self.x) // (self.square_size + self.margin))
            row = int((y - self.y) // (self.square_size + self.margin))
            index = row * self.gridsize + col

            if 0 <= index < len(self.colors):
                return self.colors[index]
        return currentcolor

    def collidemouse(self, pos):
        x, y = pos
        if (self.x <= x < self.x + self.gridsize * (self.square_size + self.margin) and
                self.y <= y < self.y + ((len(self.colors) + self.gridsize - 1) // self.gridsize) *
                (self.square_size + self.margin)):
            return True
        else:
            return False

    def transform(self):
        self.x, self.y = self.orginal_x*scalar.scalar, self.orginal_y*scalar.scalar
        self.square_size = 50*scalar.scalar
        self.Font = pygame.font.SysFont('Comic Sans MS', int(round(36 * scalar.scalar, 0)), bold=False, italic=False)
