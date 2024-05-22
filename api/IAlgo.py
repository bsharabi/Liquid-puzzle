from typing import Any, List
class IAlgo:
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
        # override this
        pass

    def is_solved(self, grid: List[List[int]], stack_height: int) -> bool:
        """
        Check if the puzzle is solved.
        
        Args:
            grid (List[List[int]]): The grid representing tubes with colored balls.
            stack_height (int): The expected height of each stack.
        
        Returns:
            bool: True if the puzzle is solved, False otherwise.
        """
        # override this
        pass

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
        # override this
        pass

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
        # override this
        pass

    def check_grid(self, grid: List[List[int]], empty: int) -> bool:
        """
        Check the validity of the grid.
        
        Args:
            grid (List[List[int]]): The grid representing tubes with colored balls.
            empty (int): Number of empty tubes.
        
        Returns:
            bool: True if the grid is valid, False otherwise.
        """
        # override this
        pass

    def check_victory(self, tubes: List[List[int]]) -> bool:
        """
        Check if the puzzle is in a victory state.
        
        Args:
            tubes (List[List[int]]): The grid representing tubes with colored balls.
        
        Returns:
            bool: True if the puzzle is solved, False otherwise.
        """
        # override this
        pass

    def __call__(self, stacksNumber: List[List[int]]) -> List[List[int]]:
        """
        Solve the liquid puzzle.
        
        Args:
            stacksNumber (List[List[int]]): The initial state of the puzzle.
        
        Returns:
            List[List[int]]: List of moves to solve the puzzle.
        """
        # override this
        pass
