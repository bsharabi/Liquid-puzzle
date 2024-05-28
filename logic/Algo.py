from api.IAlgo import *
from api.lib import *
from collections import defaultdict
import random as rd
import time
from logic.parser import Parser

def measure_time(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()  # Start time
        isSolve = func(*args, **kwargs)
        end_time = time.time()  # End time
        time_taken= end_time - start_time
        return isSolve ,f'{time_taken:.2f}Sec'
    return wrapper  

class Algo(IAlgo):
    """
    The Algo class provides a set of methods to generate tubes with colored balls,
    check and solve a liquid puzzle. It implements the IAlgo interface.
    """
    
    def __init__(self) -> None:
        """Initialize the Algo class."""
        self.df:dict[str,int | list[list[int]] | list[tuple[int]]] ={}
        self.parser = Parser()
        self.mc=0
        pass
    
    def __generate_tubes(self, full: int=4, size: int =4, colors: int = 2, empty_tube: int = 1) -> List[List[int]]:
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
            available_colors = [i for i in range(colors) for _ in range(full)]
            for i in range(size):
                for _ in range(full):
                    color = rd.choice(available_colors)
                    tubes_colors[i].append(color)
                    available_colors.remove(color)
            if self.__isSuffle(tubes_colors, size):
                break
            
        self.df = {
            "empty": empty_tube,
            "full": full,
            "size": size,
            "colors": colors,
            "tubesNumber":size+empty_tube,
            "stepToSolve": None,
            "timeTaken": None,
            "init": tubes_colors,
            "steps": None,
        }
        return tubes_colors, len(set(tubes_colors[0]))
    
    def __isSuffle(self, tubes: List[List[int]], size: int) -> bool:
        """
        Check if all tubes have the same number of different colors.
        
        Args:
            tubes (List[List[int]]): List of tubes with colored balls.
            colors (int): Number of colors.
        
        Returns:
            bool: True if all tubes have the same number of different colors, False otherwise.
        """
        return sum(1 for i in range(size - 1) if len(set(tubes[i])) == len(set(tubes[i + 1]))) == size - 1

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

    def __is_solved(self, grid: List[List[int]], stack_height: int) -> bool:
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

    def __is_valid_move(self, source_stack: List[int], destination_stack: List[int], height: int) -> bool:
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

    def __check_grid(self, grid: List[List[int]], empty: int) -> bool:
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
            print(num_balls, num_balls_expected,number_of_stacks,stack_height)
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
                if i != j and self.__is_valid_move(source_stack, destination_stack, stack_height):
                    new_grid = [list(stack) for stack in grid]
                    new_grid[j].append(new_grid[i].pop())

                    if self.__is_solved(new_grid, stack_height):
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

    def hasNext(self) -> bool:
        """
        Checks if there are more lines to read from the CSV file.

        :return: True if there are more lines, False otherwise
        """
        if hasattr(self, '_next_item'):
            return True
        try:
            self._next_item = next(self._iterator)
            return True
        except StopIteration:
            return False

    def next(self) -> dict:
        """
        Returns the next line in the CSV file as a dictionary.

        :return: A dictionary with the details of the next line
        :raises StopIteration: If there are no more items
        """
        if not self.hasNext():
            raise StopIteration("No more items")

        item = self._next_item
        del self._next_item

        # Convert CSV row to the required dictionary format
    
        return item
    
    def check_victory(self) -> bool:
        """
        Check if the puzzle is in a victory state.
        
        Args:
            tubes (List[List[int]]): The grid representing tubes with colored balls.
        
        Returns:
            bool: True if the puzzle is solved, False otherwise.
        """
        tubes=self.df["init"]
        for stack in tubes:
            if len(stack) > 0:
                if len(stack) != self.df["full"] or stack.count(stack[0]) != len(stack):
                    return False
        return True
    
    def calc_move(self, source: int, destination: int) -> bool:
        """
        Calculate the move of colors from the source tube to the destination tube.

        :param source: The index of the source tube.
        :param destination: The index of the destination tube.
        :return: True if the move is successful, False otherwise.
        """
        colors = self.df["init"]
        full = self.df["full"]
        times=0

        if colors[source]:
            color_to_move = colors[source][-1]
            if not colors[destination] or colors[destination][-1] == color_to_move:
                while colors[source] and len(colors[destination]) < full and colors[source][-1] == color_to_move:
                    colors[destination].append(colors[source].pop())
                    times+=1
                return True, [source,destination,times]
        
        return False,[]
    
    def next_grid_df(self) ->bool:
        if self.parser.hasNext():
            df =self.parser.next()
            print(df)
            self.df.update(df)
            self.df["tubesNumber"]=self.df["size"]+self.df["empty"] 
            return self()
        return False    
          
    def initialize(self,*args, filePath=None, full=None, size=None, colors=None, empty=None):
        self.mc=0
        isSolve = False
        
        while True:
            if filePath and isinstance(filePath, str) and not (full or size or colors or empty):
                self.parser.reader(filePath)
                if self.parser.hasNext():
                    df =self.parser.next()
                    print(df)
                    self.df.update(df)
                    self.df["tubesNumber"]=self.df["size"]+self.df["empty"] 
            elif full is not None and size is not None and colors is not None and empty is not None and len(args) == 0:
                self.__generate_tubes(full, size, colors, empty)
                
            elif len(args) == 1 and isinstance(args[0], bool) :
                print(self.df["init"])
                if not isSolve and self.mc==1:
                    raise ValueError("No solution to the problem was found")
                self.mc=1
            else:
                # Case: Invalid input
                raise ValueError("Invalid input provided. Please provide either a path to a file, four parameters named full, size, colors, empty, or an array of arrays followed by four parameters named full, size, colors, empty.")
            isSolve=self()
            if isSolve:
                break
        
    def __call__(self) -> bool:
        """
        Solve the liquid puzzle.
        
        Args:
            stacksNumber (List[List[int]]): The initial state of the puzzle.
        
        Returns:
            List[List[int]]: List of moves to solve the puzzle.
        """
        stacksNumber: List[List[int]] = self.df.get("init")
        
        grid = [''.join(map(str, sublist)) for sublist in stacksNumber]
        empty = sum(1 for sublist in stacksNumber if not sublist)
        stack_height = self.__get_stack_height(grid)
        print(grid,empty,stack_height)
        if self.mc==0:
            if not self.__check_grid(grid, empty):
                print("Invalid Grid")
                return False
   
            if self.__is_solved(grid, stack_height):
                print("Problem is already solved")
                return False

        visited = set()
        answer_mod = []
        memo = {}
        
        start_time = time.time()  # Start time
        isSolve =self.solve_puzzle(grid, stack_height, visited, answer_mod, memo)
        end_time = time.time()  # End time
        time_taken= end_time - start_time
        
        answer_mod.reverse()
        for v in answer_mod:
            print(f"Move {v[0] } to {v[1] } {v[2]} times")
        
        self._iterator = iter(answer_mod)
        
        if self.mc==0 and isSolve :
            self.df["stepToSolve"] = len(answer_mod)
            self.df["timeTaken"]=f'{time_taken:.2f}Sec'
            self.df["steps"] = answer_mod
            print(self.df)
            self.parser.writer(data=self.df)
            
        return isSolve 
