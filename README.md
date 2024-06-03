# Liquid Sort Puzzle

Liquid Sort is a fascinating puzzle game that challenges players to arrange colored liquids in a specific order using various containers. This README provides a simple description of the game, its objective, gameplay mechanics, rules, and difficulty.

## Objective

The objective of Liquid Sort is to arrange the colored liquids in a specific order by pouring them between containers.

## Gameplay

- Players are presented with several containers, each filled with differently colored liquids.
- Containers have limited capacities, and players can pour liquid from one container to another.
- The challenge lies in figuring out the correct sequence of pouring to achieve the desired arrangement of colors.

## Rules

1. Players can pour liquid from one container to another only if the receiving container has enough space to hold the poured liquid.
2. Liquids of different colors cannot be combined; each container can hold only one color at a time.
3. The number of pours made and the amount of liquid left in each container may affect the player's score, depending on the game's mechanics.

## Difficulty

- The difficulty of Liquid Sort puzzles can vary, with some requiring simple sequences of pours and others demanding more intricate strategies and planning.

## Components of the Heuristic
#### Total Misplaced Balls (total_misplaced):

- Definition: This counts the number of balls that are not in their correct position within their tube. Specifically, it checks if each ball matches the topmost ball in its tube.
Purpose: Balls that are out of place indicate a greater distance from the goal state, where each tube should contain balls of a single color.
Weight: Heavily weighted (3) because having balls in the correct position is critical to solving the puzzle.
Clustering Penalty (clustering_penalty):

- Definition: This penalty is based on the number of balls needed to fill a tube to its full capacity.
Purpose: Encourages the algorithm to complete tubes that are closer to being filled, thus reducing the number of partial tubes.
Weight: Moderately weighted (2) to prioritize tubes that are nearly complete.
Empty Spaces (empty_spaces):

- Definition: Counts the number of empty tubes in the grid.
Purpose: Empty tubes provide flexibility for making moves and rearranging balls, which is crucial for solving the puzzle efficiently.
Weight: Lightly weighted (1) to encourage having more empty tubes available for making moves.
Heuristic Calculation
The heuristic value is a weighted sum of the components:

```math
heuristic = (3 × total_misplaced) + (2 × clustering_penalty) − (1 × empty_spaces)

``` 

- Misplaced Balls: Prioritize reducing the number of misplaced balls.
Clustering Penalty: Favor states where tubes are closer to being completely filled.
Empty Spaces: Encourage having more empty tubes to facilitate moves.
Usage
This heuristic function is used in search algorithms like A* to prioritize states that are estimated to be closer to the goal state. By considering misplaced balls, clustering, and empty spaces, the function provides a balanced and informed estimate of the distance to the solution.

- This heuristic is designed to efficiently guide the search process towards the solution, reducing the overall time and computational resources required to solve the puzzle.



## How to run
```bash

 git clone https://github.com/bsharabi/Liquid-puzzle
 cd Liquid-puzzle

pip install -r requirements.txt

py .\Controller.py 
```