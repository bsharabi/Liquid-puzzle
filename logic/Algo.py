from api.IAlgo import *
from api.lib import *
from collections import defaultdict
import random as rd
import time

def measure_time(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()  # Start time
        result = func(*args, **kwargs)
        end_time = time.time()  # End time
        time_taken= end_time - start_time
        return result,f'{time_taken:.2f}Sec'
    return wrapper

class Algo(IAlgo):
    """
    The Algo class provides a set of methods to generate tubes with colored balls,
    check and solve a liquid puzzle. It implements the IAlgo interface.
    """
    
    def __init__(self) -> None:
        """Initialize the Algo class."""
        pass

    def generate_tubes(self, full: int, size: int, colors: int, empty_tube: int = 1) -> List[List[int]]:
        """
        Generate tubes containing colored balls ensuring each tube has the same number of different numbers.
        
        Args:
            full (int): Number of fully filled tubes.
            size (int): Number of tubes.
            colors (int): Number of colors.
            empty_tube (int, optional): Number of empty tubes. Default is 1.
        
        Returns:
            List[List[int]]: Generated tubes with colored balls.
        """
        while True:
            tubes_colors = [[] for _ in range(size + empty_tube)]
            available_colors = [i for i in range(colors) for _ in range(size)]
            for i in range(size):
                for _ in range(colors):
                    color = rd.choice(available_colors)
                    tubes_colors[i].append(color)
                    available_colors.remove(color)
            if self.__isSuffle(tubes_colors, colors):
                break
        return tubes_colors, len(set(tubes_colors[0]))

    def __isSuffle(self, tubes: List[List[int]], colors: int) -> bool:
        """
        Check if all tubes have the same number of different colors.
        
        Args:
            tubes (List[List[int]]): List of tubes with colored balls.
            colors (int): Number of colors.
        
        Returns:
            bool: True if all tubes have the same number of different colors, False otherwise.
        """
        return sum(1 for i in range(colors - 1) if len(set(tubes[i])) == len(set(tubes[i + 1]))) == colors - 1

    def __get_stack_height(self, grid: List[List[int]]) -> int:
        """
        Get the maximum height of stacks in the grid.
        
        Args:
            grid (List[List[int]]): The grid representing tubes with colored balls.
        
        Returns:
            int: Maximum height of stacks in the grid.
        """
        return max(len(stack) for stack in grid)

    def __canonical_string_conversion(self, grid: List[List[int]]) -> str:
        """
        Convert the grid to a canonical string representation.
        
        Args:
            grid (List[List[int]]): The grid representing tubes with colored balls.
        
        Returns:
            str: Canonical string representation of the grid.
        """
        return ";".join(",".join(map(str, stack)) for stack in grid)

    def is_solved(self, grid: List[List[int]], stack_height: int) -> bool:
        """
        Check if the puzzle is solved.
        
        Args:
            grid (List[List[int]]): The grid representing tubes with colored balls.
            stack_height (int): The expected height of each stack.
        
        Returns:
            bool: True if the puzzle is solved, False otherwise.
        """
        for stack in grid:
            if not stack:
                continue
            if len(stack) != stack_height or stack.count(stack[0]) != stack_height:
                return False
        return True

    def is_valid_move(self, source_stack: List[int], destination_stack: List[int], height: int) -> bool:
        """
        Check if moving a ball from source stack to destination stack is valid.
        
        Args:
            source_stack (List[int]): The source stack.
            destination_stack (List[int]): The destination stack.
            height (int): The maximum height of a stack.
        
        Returns:
            bool: True if the move is valid, False otherwise.
        """
        if not source_stack or len(destination_stack) == height:
            return False

        if not destination_stack or source_stack[-1] == destination_stack[-1]:
            if not destination_stack:
                color_freqs = source_stack.count(source_stack[0])
                if color_freqs == len(source_stack):
                    return False
            return True
        return False

    def solve_puzzle(self, grid: List[List[int]], stack_height: int, visited: set, answer_mod: List[List[int]], memo: dict) -> bool:
        """
        Solve the liquid puzzle using backtracking.
        
        Args:
            grid (List[List[int]]): The grid representing tubes with colored balls.
            stack_height (int): The expected height of each stack.
            visited (set): Set of visited grid states.
            answer_mod (List[List[int]]): List of moves to solve the puzzle.
            memo (dict): Memoization dictionary for storing already computed states.
        
        Returns:
            bool: True if the puzzle is solved, False otherwise.
        """
        canonical_grid = self.__canonical_string_conversion(grid)
        if canonical_grid in memo:
            return memo[canonical_grid]

        if stack_height == -1:
            stack_height = self.__get_stack_height(grid)

        if canonical_grid in visited:
            return False

        visited.add(canonical_grid)

        for i, source_stack in enumerate(grid):
            for j, destination_stack in enumerate(grid):
                if i != j and self.is_valid_move(source_stack, destination_stack, stack_height):
                    new_grid = [list(stack) for stack in grid]
                    new_grid[j].append(new_grid[i].pop())

                    if self.is_solved(new_grid, stack_height):
                        answer_mod.append([i, j, 1])
                        memo[canonical_grid] = True
                        return True

                    if self.solve_puzzle(new_grid, stack_height, visited, answer_mod, memo):
                        if answer_mod and answer_mod[-1][0] == i and answer_mod[-1][1] == j:
                            answer_mod[-1][2] += 1
                        else:
                            answer_mod.append([i, j, 1])
                        memo[canonical_grid] = True
                        return True

        memo[canonical_grid] = False
        return False

    def check_grid(self, grid: List[List[int]], empty: int) -> bool:
        """
        Check the validity of the grid.
        
        Args:
            grid (List[List[int]]): The grid representing tubes with colored balls.
            empty (int): Number of empty tubes.
        
        Returns:
            bool: True if the grid is valid, False otherwise.
        """
        number_of_stacks = len(grid)
        stack_height = self.__get_stack_height(grid)
        num_balls_expected = (number_of_stacks - empty) * stack_height
        num_balls = sum(len(stack) for stack in grid)

        if num_balls != num_balls_expected:
            print("Grid has incorrect # of balls")
            return False

        ball_color_frequency = defaultdict(int)
        for stack in grid:
            for ball in stack:
                ball_color_frequency[ball] += 1

        for ball_color, frequency in ball_color_frequency.items():
            if frequency != stack_height:
                print(f"Color {ball_color} is not {stack_height}")
                return False

        return True

    def check_victory(self, tubes: List[List[int]]) -> bool:
        """
        Check if the puzzle is in a victory state.
        
        Args:
            tubes (List[List[int]]): The grid representing tubes with colored balls.
        
        Returns:
            bool: True if the puzzle is solved, False otherwise.
        """
        for stack in tubes:
            if len(stack) > 0:
                if len(stack) != self.size or stack.count(stack[0]) != len(stack):
                    return False
        return True
    
    @measure_time
    def __call__(self, stacksNumber: List[List[int]]) -> List[List[int]]:
        """
        Solve the liquid puzzle.
        
        Args:
            stacksNumber (List[List[int]]): The initial state of the puzzle.
        
        Returns:
            List[List[int]]: List of moves to solve the puzzle.
        """
        grid = [''.join(map(str, sublist)) for sublist in stacksNumber]
        empty = sum(1 for sublist in stacksNumber if not sublist)
        print(grid)

        if not self.check_grid(grid, empty):
            print("Invalid Grid")
            return []

        stack_height = self.__get_stack_height(grid)
        if self.is_solved(grid, stack_height):
            print("Problem is already solved")
            return []

        visited = set()
        answer_mod = []
        memo = {}

        self.solve_puzzle(grid, stack_height, visited, answer_mod, memo)

        answer_mod.reverse()
        for v in answer_mod:
            print(f"Move {v[0] + 1} to {v[1] + 1} {v[2]} times")
        return answer_mod
