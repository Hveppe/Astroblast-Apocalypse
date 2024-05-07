# Spillet er lavet af Hveppe

import pygame
pygame.mixer.init()


class Button:
    clickbuttonsound = pygame.mixer.Sound("sound/click-menu-app-147357.wav")

    def __init__(self, screen, tekst, size, image):
        self.tekst = tekst
        self.size = size
        self.image = image
        self.screen = screen
        self.clicked = False
        self.action = True

        self.width, self.height = size

        self.image = pygame.transform.scale(self.image, size)
        self.image_rect = None

        self.x, self.y = 0, 0

    def draw(self, x, y):
        self.action = False
        self.x = x
        self.y = y

        self.image_rect = self.image.get_rect(topleft=(self.x, self.y))

        # check om musen er over knappen og om der trykkes på den
        if self.image_rect.collidepoint(pygame.mouse.get_pos()):
            if pygame.mouse.get_pressed()[0] == 1 and self.clicked is False:
                self.clicked = True
                self.clickbuttonsound.play()

            if pygame.mouse.get_pressed()[0] == 0 and self.clicked is True:
                self.clicked = False
                self.action = True

        # tegn knappen
        self.screen.blit(self.image, self.image.get_rect(topleft=(self.x, self.y)))
        font = pygame.font.SysFont('Comic Sans MS', 40)
        tekstdisplay = font.render(self.tekst, True, (255, 255, 255))
        self.screen.blit(tekstdisplay, (self.image_rect.x + self.image_rect.width/2 - tekstdisplay.get_width()/2,
                         self.image_rect.y + self.image_rect.height/2-tekstdisplay.get_height()/2))

        return self.action


class Picture:
    def __init__(self, screen, x, y, image):
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
        self.screen = screen

    def draw(self):
        self.screen.blit(self.image, self.rect.center)


class AstroidClass:
    color = (187, 188, 188)

    def __init__(self, screen, xvalue, yvalue, speed, radius, direction):
        self.screen = screen
        self.x = xvalue
        self.y = yvalue
        self.radius = radius
        self.speed = speed
        self.direction = direction

        self.width = radius * 2
        self.height = radius * 2

    def move(self):
        if self.direction == 1:
            self.y += self.speed
        if self.direction == 2:
            self.x += self.speed
        if self.direction == 3:
            self.y -= self.speed
        if self.direction == 4:
            self.x -= self.speed

    def draw(self):
        pygame.draw.circle(surface=self.screen, color=self.color, center=(self.x, self.y), radius=self.radius)
