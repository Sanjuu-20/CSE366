import pygame
class Environment:
    def __init__(self,w,h):
        pygame.init()
        self.w = w
        self.h = h
        self.screen = pygame.display.set_mode((self.w, self.h))
        pygame.display.set_caption("Pygame AI Simulation Framework Assignment")
        self.font = pygame.font.Font(None, 36)
    

    def limit_position(self, x, y):
        if x < 0 :
            x = 0
        if x > self.w :
            x = self.w
        if y < 0 :
            y = 0
        if y > self.h :
            y = self.h
        return x,y