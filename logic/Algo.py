from api.IAlgo import *
from api.lib import *
from collections import defaultdict
import random as rd
import time
from logic.parser import Parser
import heapq
from copy import deepcopy

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
        # return sum(1 for i in range(size - 1) if len(set(tubes[i])) == len(set(tubes[i + 1]))) == size - 1
        return True

    def __get_stack_height(self, grid: List[List[int]]) -> int:
        """
        Get the maximum height of stacks in the grid.
        
        Args:
            grid (List[List[int]]): The grid representing tubes with colored balls.
        
        Returns:
            int: Maximum height of stacks in the grid.
        """
        return max(len(stack) for stack in grid)

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

    def solve_puzzle(self,init: list[list[int]], full: int) -> list[list[int]] | None:
        def is_solved(grid: list[list[int]]) -> bool:
            return all(len(stack) == full and stack.count(stack[0]) == full for stack in grid if stack)

        def canonical_string_conversion(grid: list[list[int]]) -> str:
            return ";".join(",".join(map(str, stack)) for stack in grid)

        def is_visit(grid: list[list[int]]) -> bool:
            canonical_grid = canonical_string_conversion(grid)
            if canonical_grid in visited:
                return True
            visited.add(canonical_grid)
            return False

        def get_color_sequence_number(tube: list[int], color: int) -> int:
            sequence_cnt = 0
            for tube_color in reversed(tube):
                if tube_color != color:
                    break
                sequence_cnt += 1
            return sequence_cnt

        def get_sequences(color: int, grid: list[list[int]]) -> list[list[int]]:
            steps = []
            for index, tube in enumerate(grid):
                if tube:
                    sequence = get_color_sequence_number(tube, color)
                    if sequence:
                        steps.append([index, -1, sequence])
            return steps

        def get_head_tubes(grid: list[list[int]]) -> set[int]:
            return {tube[-1] for tube in grid if tube and not (len(tube) == full and tube.count(tube[0]) == full)}

        def calc_move(steps_list: list[list[int]], grid: list[list[int]], steps: list[list[int]]) -> bool:
            child_grid = deepcopy(grid)
            child_steps = deepcopy(steps)
            cnt_to_transfer = sum(step[2] for step in steps_list)
            dest = child_grid[steps_list[0][1]]
            if len(dest) + cnt_to_transfer > full:
                return False
            for step in steps_list:
                for _ in range(step[2]):
                    src = child_grid[step[0]].pop()
                    dest.append(src)
                child_steps.append(step)
            if not is_visit(child_grid):
                heapq.heappush(priority_queue, (calculate_heuristic(child_grid), child_grid, child_steps))
                return True
            return False

        def find_empty_tube(grid: list[list[int]]) -> int:
            for i, tube in enumerate(grid):
                if not tube:
                    return i
            return -1

        def find_all_max_sequences_to_movement(grid: list[list[int]]) -> list[list[list[int]]]:
            empty_tube_index = find_empty_tube(grid)
            if empty_tube_index == -1:
                return []
            heads = get_head_tubes(grid)
            max_sequences = 0
            list_all_max_sequences_steps = []
            for color in heads:
                steps = get_sequences(color, grid)
                if steps:
                    calc_sequences = sum(step[2] for step in steps)
                    if max_sequences > calc_sequences:
                        continue
                    if max_sequences < calc_sequences:
                        max_sequences = calc_sequences
                        list_all_max_sequences_steps.clear()
                    list_all_max_sequences_steps.append(
                        [list(map(lambda item: empty_tube_index if item == -1 else item, sublist)) for sublist in steps]
                    )
            return list_all_max_sequences_steps

        def get_new_configuration_for_an_empty_tube(grid: list[list[int]], steps: list[list[int]]) -> bool:
            steps_lists = find_all_max_sequences_to_movement(grid)
            has_new_configuration = False
            for steps_list in steps_lists:
                if calc_move(steps_list, grid, steps):
                    has_new_configuration = True
            return has_new_configuration

        def get_internal_arrangement(grid: list[list[int]], steps: list[list[int]]) -> bool:
            def get_list_incomplete_tubes(grid: list[list[int]]) -> list[list[int]]:
                transfer_lists = []
                for index, tube in enumerate(grid):
                    if tube and not (len(tube) == full and tube.count(tube[0]) == full) and len(tube) < full:
                        color = tube[-1]
                        transfer_lists.append([index, color, full - len(tube)])
                return transfer_lists

            def get_list_transfer_tubes(grid: list[list[int]]) -> list[list[list[int]]]:
                heads = get_head_tubes(grid)
                list_all_sequences_steps = []
                for color in heads:
                    steps = get_sequences(color, grid)
                    if steps:
                        list_all_sequences_steps.append(
                            [list(map(lambda item: color if item == -1 else item, sublist)) for sublist in steps]
                        )
                return list_all_sequences_steps

            incomplete_list = get_list_incomplete_tubes(grid)
            transfer_lists = get_list_transfer_tubes(grid)

            new_steps = []
            has_new_configuration = False
            for incomplete in incomplete_list:
                dest, dest_color, space = incomplete
                for transfer_list in transfer_lists:
                    space_available = space
                    new_steps.clear()
                    for transfer in transfer_list:
                        src, src_color, amount = transfer
                        if dest_color != src_color or dest == src:
                            continue
                        if space_available >= amount:
                            new_steps.append([src, dest, amount])
                            space_available -= amount
                            has_new_configuration = True
                        else:
                            if new_steps:
                                calc_move(new_steps, grid, steps)
                            space_available = space - amount
                            new_steps.clear()
                            new_steps.append([src, dest, amount])
                    if new_steps:
                        calc_move(new_steps, grid, steps)
            return has_new_configuration

        def calculate_heuristic(grid: list[list[int]]) -> int:
            total_misplaced = 0
            clustering_penalty = 0
            empty_spaces = 0
            potential_moves = 0

            for tube in grid:
                if not tube:
                    empty_spaces += 1
                    continue
                
                color = tube[0]
                correct_sequence = True
                for i in range(len(tube)):
                    if tube[i] != color:
                        correct_sequence = False
                        total_misplaced += 1

                if correct_sequence and len(tube) < full:
                    clustering_penalty += (full - len(tube))
                
                # Count potential moves
                if len(tube) > 0 and not correct_sequence:
                    potential_moves += 1

            # Weighting factors for each component of the heuristic
            misplaced_weight = 5
            clustering_weight = 3
            empty_spaces_weight = 2
            potential_moves_weight = 1

            heuristic = (
                misplaced_weight * total_misplaced +
                clustering_weight * clustering_penalty -
                empty_spaces_weight * empty_spaces +
                potential_moves_weight * potential_moves
            )

            return heuristic


        priority_queue = []
        heapq.heappush(priority_queue, (calculate_heuristic(init), init, []))
        visited = set()
        is_visit(init)

        while priority_queue:
            _, grid, steps = heapq.heappop(priority_queue)
            if is_solved(grid):
                return steps
            if get_internal_arrangement(grid, steps):
                continue
            if not get_new_configuration_for_an_empty_tube(grid, steps):
                continue

        return None

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
                print("f")
                
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
        grid: List[List[int]] = self.df.get("init")
        
        empty = sum(1 for sublist in grid if not sublist)
        stack_height = self.__get_stack_height(grid)
        print(grid,empty,stack_height)
        if self.mc==0:
            if not self.__check_grid(grid, empty):
                print("Invalid Grid")
                return False
   
            if self.__is_solved(grid, stack_height):
                print("Problem is already solved")
                return False

      
        start_time = time.time()  # Start time
        answer_mod =self.solve_puzzle(grid, stack_height)
        end_time = time.time()  # End time
        time_taken= end_time - start_time
        isSolve= True if answer_mod else False
        if not isSolve:
            return False
        
        for v in answer_mod:
            print(f"Move {v[0] } to {v[1] } {v[2]} times")
        
        self._iterator = iter(answer_mod)
        if self.mc==0 and isSolve :
            self.df["stepToSolve"] = len(answer_mod)
            self.df["timeTaken"]=f'{time_taken:.2f}Sec'
            self.df["steps"] = answer_mod
            self.parser.writer(data=self.df)
            
        return isSolve 



