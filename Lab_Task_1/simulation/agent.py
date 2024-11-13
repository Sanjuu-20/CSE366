import pygame
from environment import Environment
class Agent(pygame.sprite.Sprite):
    AGENT_COLOR = (0, 128, 255) 
    def __init__(self, x, y, speed, ement):
        super().__init__()
        self.image = pygame.Surface((30, 30))
        self.image.fill(Agent.AGENT_COLOR)
        self.rect = self.image.get_rect()
        self.rect.x, self.rect.y = x, y
        self.speed = speed
        self.ement=ement

    def move(self, keys):
        if keys[pygame.K_LEFT]:
            self.rect.x = (self.rect.x - self.speed + self.ement.w) % self.ement.w
            self.speed += 2
        if keys[pygame.K_RIGHT]:
            self.rect.x = (self.rect.x + self.speed + self.ement.w) % self.ement.w
            self.speed += 2
        if keys[pygame.K_UP]:
            self.rect.y = (self.rect.y - self.speed + self.ement.h) % self.ement.h
            self.speed += 2
        if keys[pygame.K_DOWN]:
            self.rect.y = (self.rect.y + self.speed + self.ement.h) % self.ement.h
            self.speed += 2
        temp_x, temp_y = self.ement.limit_position(self.rect.x, self.rect.y)
        self.rect.x, self.rect.y = temp_x, temp_y 
