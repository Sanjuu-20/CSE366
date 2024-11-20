# Lab Task -2 : Simulation of UCS and A* Algorithms for Pathfinding

This project is an interactive grid based simulation implemented in Pygame, showcasing AI agents navigating a grid environment to complete tasks. The agents employ Uniform Cost Search (UCS) and A Search* algorithms to find optimal paths to their respective tasks while avoiding obstacles.


## Algorithms Used

### Uniform Cost Search (UCS)
* The agent explores paths in order of increasing cumulative cost.
* It guarantees finding the optimal path by always expanding the least costly node first.
* In this simulation, Agent uses UCS to navigate the grid and complete tasks.


### A* Search
* A* combines the benefits of UCS and heuristic-driven search.
* It uses a cost function f(n)=g(n)+h(n), where:
  * g(n) is the cost from the start to the current node.
  * h(n) is the heuristic estimate of the cost from the current node to the goal.
* The Manhattan distance is used as the heuristic in this project, making A* efficient for grid-based environments.
* Agent uses A* for task completion.


## How to Run

1. If pygame is not installed, install pygame using ```pip install pygame```.

2. Run the run.py file to start the simulation ```python run.py```.


## Key Components


### **`agent.py`**
Defines the `Agent` class, responsible for navigation, task-solving, and implementing search algorithms.

- **Key Components**:
  - **Initialization**:
    - Sets up the agent's position, appearance, and default algorithm (A* or UCS).
  - **Movement Logic**:
    - Moves the agent step-by-step along a computed path.
    - Tracks task completion and path cost.
  - **Pathfinding Algorithms**:
    - **A***:
      - Combines path cost(g) and heuristic(h) to efficiently find paths.
    - **UCS**:
      - Explores paths based on cumulative costs, ensuring optimal solutions.
  - **Helper Methods**:
    - `get_neighbors()`: Identifies valid neighboring cells.
    - `heuristic()`: Uses Manhattan distance for A* calculations.

---

### **`environment.py`**
Defines the grid environment, including task and barrier placement.

- **Key Components**:
  - **Grid Setup**:
    - Defines dimensions, task, and barrier counts.
  - **Task and Barrier Generation**:
    - Generates unique random positions for tasks and barriers.
  - **Validation Methods**:
    - `is_within_bounds()`: Ensures coordinates stay within the grid.
    - `is_barrier()`: Checks if a coordinate is a barrier.

---

### **`run.py`**
Manages the simulation using **pygame** and visualizes agent interactions with the environment.

- **Key Components**:
  - **Environment Initialization**:
    - Creates the grid, tasks, barriers, and two agents.
  - **Agent Control**:
    - Includes buttons for running:
      - **Agent 1** with **UCS**.
      - **Agent 2** with **A***.
  - **Visualization**:
    - Displays the grid, tasks, barriers, and agents in real-time.
    - Updates the status panel with:
      - Task progress.
      - Agent positions.
      - Path cost and completed tasks.
  - **Event Handling**:
    - Responds to user interactions (e.g., button clicks).
  - **Game Loop**:
    - Updates agent movements and UI in real-time.
  - **Execution**:
    - Launches the simulation through the `main()` function.


## Customization

You can modify the grid size, number of tasks, and barriers by editing the constants in the run.py file.

