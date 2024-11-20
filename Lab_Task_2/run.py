import pygame
import sys
import copy
from agent import Agent
from environment import Environment

# Constants
WINDOW_WIDTH, WINDOW_HEIGHT = 800, 600
GRID_SIZE = 40
STATUS_WIDTH = 500
BACKGROUND_COLOR = (255, 255, 255)
BARRIER_COLOR = (0, 0, 0)  # Barrier color is black
TASK_COLOR = (255, 0, 0)   # Task color is red
VISITED_TASK_COLOR = (0, 255, 0)  # Task color turns green after visit
TEXT_COLOR = (0, 0, 0)
BUTTON_COLOR = (0, 200, 0)
BUTTON_HOVER_COLOR = (0, 255, 0)
UCS_BUTTON_COLOR = (255, 165, 0)     # Orange button for UCS
A_STAR_BUTTON_COLOR = (0, 100, 255)  # Blue button for A*
BUTTON_TEXT_COLOR = (255, 255, 255)
MOVEMENT_DELAY = 200  # Milliseconds between movements

def reset_task_colors(environment):
    """Reset all task colors to red when starting Agent 2 or Agent 1."""
    return {location: TASK_COLOR for location in environment.task_locations}

def main():
    pygame.init()

    # Set up display with an additional status panel
    screen = pygame.display.set_mode((WINDOW_WIDTH + STATUS_WIDTH, WINDOW_HEIGHT))
    pygame.display.set_caption("Pygame AI Grid Simulation with Two Agents")

    # Clock to control frame rate
    clock = pygame.time.Clock()
    font = pygame.font.Font(None, 20)

    # Initialize environment and agents
    original_environment = Environment(WINDOW_WIDTH, WINDOW_HEIGHT, GRID_SIZE, num_tasks=5, num_barriers=15)
    environment1 = copy.deepcopy(original_environment)
    environment2 = copy.deepcopy(original_environment)

    agent1 = Agent(environment1, GRID_SIZE)
    agent2 = Agent(environment2, GRID_SIZE)
    all_sprites = pygame.sprite.Group(agent1, agent2)

    # Buttons for running UCS for Agent 1 and A* for Agent 2
    button_width, button_height = 150, 50
    ucs_button_x = WINDOW_WIDTH + 50
    a_star_button_x = WINDOW_WIDTH + 250
    ucs_button_y = WINDOW_HEIGHT - 100
    a_star_button_y = WINDOW_HEIGHT - 100

    ucs_button = pygame.Rect(ucs_button_x, ucs_button_y, button_width, button_height)
    a_star_button = pygame.Rect(a_star_button_x, a_star_button_y, button_width, button_height)

    # Variables for movement delay
    last_move_time = pygame.time.get_ticks()

    # Flags to track algorithm status for each agent
    agent1_running = False
    agent2_running = False

    # Task colors dictionary to manage task colors
    task_colors = {location: TASK_COLOR for location in original_environment.task_locations}

    # Main loop
    running = True
    while running:
        clock.tick(60)  # Limit to 60 FPS

        # Event handling
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            if event.type == pygame.MOUSEBUTTONDOWN:
                if ucs_button.collidepoint(event.pos):
                    # Reset task colors to red when Agent 1 starts
                    task_colors = reset_task_colors(environment1)
                    agent1.set_algorithm("UCS")
                    agent1_running = True
                    if environment1.task_locations:
                        agent1.find_nearest_task()
                elif a_star_button.collidepoint(event.pos):
                    # Reset task colors to red when Agent 2 starts
                    task_colors = reset_task_colors(environment2)
                    agent2.set_algorithm("A*")
                    agent2_running = True
                    agent2.find_nearest_task()

        # Clear the screen
        screen.fill(BACKGROUND_COLOR)

        # Draw grid and barriers
        for x in range(original_environment.columns):
            for y in range(original_environment.rows):
                rect = pygame.Rect(x * GRID_SIZE, y * GRID_SIZE, GRID_SIZE, GRID_SIZE)
                pygame.draw.rect(screen, (200, 200, 200), rect, 1)  # Draw grid lines

        # Draw barriers
        for (bx, by) in original_environment.barrier_locations:
            barrier_rect = pygame.Rect(bx * GRID_SIZE, by * GRID_SIZE, GRID_SIZE, GRID_SIZE)
            pygame.draw.rect(screen, BARRIER_COLOR, barrier_rect)

        # Draw tasks with current colors
        for (tx, ty), task_number in original_environment.task_locations.items():
            task_rect = pygame.Rect(tx * GRID_SIZE, ty * GRID_SIZE, GRID_SIZE, GRID_SIZE)
            pygame.draw.rect(screen, task_colors[(tx, ty)], task_rect)
            task_num_surface = font.render(str(task_number), True, (255, 255, 255))
            task_num_rect = task_num_surface.get_rect(center=task_rect.center)
            screen.blit(task_num_surface, task_num_rect)

        status_x = WINDOW_WIDTH + 10
        algo_text = "Algorithm : UCS"
        task_status_text = f"Tasks Completed: {agent1.task_completed}"
        position_text = f"Position: {agent1.position}"
        completed_tasks_text = f"Completed Tasks: "
        task_list_text = f"{agent1.completed_tasks}"
        path_cost_text = f"Path Cost: {agent1.path_cost}"

        algo_surface = font.render(algo_text, True, TEXT_COLOR)
        status_surface = font.render(task_status_text, True, TEXT_COLOR)
        position_surface = font.render(position_text, True, TEXT_COLOR)
        completed_tasks_surface = font.render(completed_tasks_text, True, TEXT_COLOR)
        task_list_surface = font.render(task_list_text, True, TEXT_COLOR)
        path_cost_surface = font.render(path_cost_text, True, TEXT_COLOR)

        screen.blit(algo_surface, (status_x, 20))
        screen.blit(status_surface, (status_x, 50))
        screen.blit(position_surface, (status_x, 80))
        screen.blit(completed_tasks_surface, (status_x, 110))
        screen.blit(task_list_surface, (status_x, 140))
        screen.blit(path_cost_surface, (status_x, 170))

        algo_text2 = "Algorithm : A*"
        task_status_text2 = f"Tasks Completed: {agent2.task_completed}"
        position_text2 = f"Position: {agent2.position}"
        completed_tasks_text2 = f"Completed Tasks: "
        task_list_text2 = f"{agent2.completed_tasks}"
        path_cost_text2 = f"Path Cost: {agent2.path_cost}"

        algo_surface = font.render(algo_text2, True, TEXT_COLOR)
        status_surface = font.render(task_status_text2, True, TEXT_COLOR)
        position_surface = font.render(position_text2, True, TEXT_COLOR)
        completed_tasks_surface = font.render(completed_tasks_text2, True, TEXT_COLOR)
        task_list_surface = font.render(task_list_text2, True, TEXT_COLOR)
        path_cost_surface = font.render(path_cost_text2, True, TEXT_COLOR)

        screen.blit(algo_surface, (status_x, 220))
        screen.blit(status_surface, (status_x, 250))
        screen.blit(position_surface, (status_x, 280))
        screen.blit(completed_tasks_surface, (status_x, 310))
        screen.blit(task_list_surface, (status_x, 340))
        screen.blit(path_cost_surface, (status_x, 370))

        # Draw agents
        all_sprites.draw(screen)

        # Update agents' movements
        current_time = pygame.time.get_ticks()
        if current_time - last_move_time > MOVEMENT_DELAY:
            if agent1_running:
                if not agent1.moving and environment1.task_locations:
                    agent1.find_nearest_task()
                elif agent1.moving:
                    agent1.move()
                    # Change visited task color to green
                    if tuple(agent1.position) in task_colors:
                        task_colors[tuple(agent1.position)] = VISITED_TASK_COLOR

            if agent2_running:
                if not agent2.moving and original_environment.task_locations:
                    agent2.find_nearest_task()
                elif agent2.moving:
                    agent2.move()
                    # Change visited task color to green
                    if tuple(agent2.position) in task_colors:
                        task_colors[tuple(agent2.position)] = VISITED_TASK_COLOR

            last_move_time = current_time

        # Draw buttons
        pygame.draw.rect(screen, UCS_BUTTON_COLOR, ucs_button)
        ucs_text = font.render("Run UCS", True, BUTTON_TEXT_COLOR)
        ucs_text_rect = ucs_text.get_rect(center=ucs_button.center)
        screen.blit(ucs_text, ucs_text_rect)

        pygame.draw.rect(screen, A_STAR_BUTTON_COLOR, a_star_button)
        a_star_text = font.render("Run A*", True, BUTTON_TEXT_COLOR)
        a_star_text_rect = a_star_text.get_rect(center=a_star_button.center)
        screen.blit(a_star_text, a_star_text_rect)

        # Draw the status panel separator
        pygame.draw.line(screen, (0, 0, 0), (WINDOW_WIDTH, 0), (WINDOW_WIDTH, WINDOW_HEIGHT))

        # Update the display
        pygame.display.flip()

    # Quit Pygame properly
    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()
