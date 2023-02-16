import pygame, random


class Comet:
    def __init__(self, screen_width, comet_img):
        self.image = comet_img
        self.width, self.height = comet_img.get_size()
        self.x = random.randint(0, screen_width - self.width)
        self.y = -self.height
        self.speed = random.randint(6, 8)/10

    def update(self):
        self.y += self.speed

    def draw(self, screen):
        screen.blit(self.image, (self.x, self.y))
