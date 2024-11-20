import pygame
import heapq

class Agent(pygame.sprite.Sprite):
    def __init__(self, environment, grid_size):
        super().__init__()
        self.image = pygame.Surface((grid_size, grid_size))
        self.image.fill((0, 0, 255))  # Agent color is blue
        self.rect = self.image.get_rect()
        self.grid_size = grid_size
        self.environment = environment
        self.position = [0, 0]  # Starting at the top-left corner of the grid
        self.rect.topleft = (0, 0)
        self.task_completed = 0
        self.completed_tasks = []
        self.moving = False  # Flag to indicate if the agent is moving
        self.path_cost = 0  # Cost of the current path
        self.last_cost = 0
        self.path = []
        self.algorithm = "A*"  # Default algorithm
        self.task_locations = self.environment.task_locations

    def set_algorithm(self, algorithm):
        """Set the search algorithm (A* or UCS)."""
        self.algorithm = algorithm

    def move(self):
        """Move the agent along the path."""
        if self.path:
            next_position = self.path.pop(0)
            self.position = list(next_position)
            self.rect.topleft = (self.position[0] * self.grid_size, self.position[1] * self.grid_size)
            self.path_cost += 1
            self.check_task_completion()
        else:
            self.moving = False  # Stop moving when path is exhausted

    def check_task_completion(self):
        """Check if the agent has reached a task location."""
        position_tuple = tuple(self.position)
        if position_tuple in self.task_locations:
            task_number = self.task_locations.pop(position_tuple)
            self.task_completed += 1
            self.completed_tasks.append((task_number, f"Cost = {self.path_cost - self.last_cost}"))
            self.last_cost = self.path_cost

    def find_nearest_task(self):
        """Find the nearest task using the selected algorithm."""
        nearest_task = None
        shortest_path = None
        lowest_cost = float('inf')

        for task_position in self.task_locations.keys():
            path, cost = self.find_path_to(task_position)
            if path and cost < lowest_cost:
                shortest_path = path
                lowest_cost = cost
                nearest_task = task_position

        if shortest_path:
            self.path = shortest_path[1:]  # Exclude the current position
            self.moving = True

    def find_path_to(self, target):
        """Find a path to the target using the selected algorithm."""
        if self.algorithm == "A*":
            return self.a_star_search(target)
        elif self.algorithm == "UCS":
            return self.uniform_cost_search(target)

    def a_star_search(self, goal):
        """A* Search implementation."""
        start = tuple(self.position)

        open_set = []
        heapq.heappush(open_set, (0, start, [start]))
        g_scores = {start: 0}

        while open_set:
            _, current, path = heapq.heappop(open_set)

            if current == goal:
                return path, g_scores[current]

            for neighbor in self.get_neighbors(*current):
                tentative_g_score = g_scores[current] + 1  # Uniform cost of 1 per move
                if neighbor not in g_scores or tentative_g_score < g_scores[neighbor]:
                    g_scores[neighbor] = tentative_g_score
                    f_score = tentative_g_score + self.heuristic(neighbor, goal)
                    heapq.heappush(open_set, (f_score, neighbor, path + [neighbor]))

        return None, float('inf')  # No path found

    def uniform_cost_search(self, goal):
        """UCS implementation."""
        start = tuple(self.position)

        open_set = []
        heapq.heappush(open_set, (0, start, [start]))
        visited = set()

        while open_set:
            cost, current, path = heapq.heappop(open_set)

            if current == goal:
                return path, cost

            if current not in visited:
                visited.add(current)
                for neighbor in self.get_neighbors(*current):
                    heapq.heappush(open_set, (cost + 1, neighbor, path + [neighbor]))

        return None, float('inf')  # No path found

    def heuristic(self, a, b):
        """Manhattan distance heuristic."""
        (x1, y1) = a
        (x2, y2) = b
        return abs(x1 - x2) + abs(y1 - y2)

    def get_neighbors(self, x, y):
        """Get walkable neighboring positions."""
        neighbors = []
        directions = [("up", (0, -1)), ("down", (0, 1)), ("left", (-1, 0)), ("right", (1, 0))]
        for _, (dx, dy) in directions:
            nx, ny = x + dx, y + dy
            if self.environment.is_within_bounds(nx, ny) and not self.environment.is_barrier(nx, ny):
                neighbors.append((nx, ny))
        return neighbors
