import pygame
import sys
from agent import Agent
from environment import Environment

BACKGROUND_COLOR = (255, 255, 255)
TEXT_COLOR = (0, 0, 0)

ement = Environment(700, 500)
agent = Agent(0, 0, 5, ement)
all_sprites = pygame.sprite.Group()
all_sprites.add(agent)
clock = pygame.time.Clock()
running = True
while running:
    clock.tick(30)

    keys = pygame.key.get_pressed()
    
    agent.move(keys)

    ement.screen.fill(BACKGROUND_COLOR)

    all_sprites.draw(ement.screen)

    frame_text = ement.font.render(f"Position: {agent.rect.x}, {agent.rect.y}", True, TEXT_COLOR)
    ement.screen.blit(frame_text, (10, 10))

    frame_text2 = ement.font.render(f"Speed: {agent.speed}", True, TEXT_COLOR)
    ement.screen.blit(frame_text2, (10, 30))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    pygame.display.flip()

pygame.quit()
sys.exit()
