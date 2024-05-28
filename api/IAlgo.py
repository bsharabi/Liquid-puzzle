from typing import Any, List
class IAlgo:
    """
    The Algo class provides a set of methods to generate tubes with colored balls,
    check and solve a liquid puzzle. It implements the IAlgo interface.
    """  

    
    def __init__(self) -> None:
        """Initialize the Algo class."""
        self.df=None
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
        # override this
        pass      
    
    def __isSuffle(self, tubes: List[List[int]], size: int) -> bool:
        """
        Check if all tubes have the same number of different colors.
        
        Args:
            tubes (List[List[int]]): List of tubes with colored balls.
            colors (int): Number of colors.
        
        Returns:
            bool: True if all tubes have the same number of different colors, False otherwise.
        """
        # override this
        pass       

    def __get_stack_height(self, grid: List[List[int]]) -> int:
        """
        Get the maximum height of stacks in the grid.
        
        Args:
            grid (List[List[int]]): The grid representing tubes with colored balls.
        
        Returns:
            int: Maximum height of stacks in the grid.
        """
        # override this
        pass       

    def __canonical_string_conversion(self, grid: List[List[int]]) -> str:
        """
        Convert the grid to a canonical string representation.
        
        Args:
            grid (List[List[int]]): The grid representing tubes with colored balls.
        
        Returns:
            str: Canonical string representation of the grid.
        """
        # override this
        pass        

    def __is_solved(self, grid: List[List[int]], stack_height: int) -> bool:
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
        # override this
        pass        

    def __check_grid(self, grid: List[List[int]], empty: int) -> bool:
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

    def hasNext(self) -> bool:
        """
        Checks if there are more lines to read from the CSV file.

        :return: True if there are more lines, False otherwise
        """
        # override this
        pass   

    def next(self) -> dict:
        """
        Returns the next line in the CSV file as a dictionary.

        :return: A dictionary with the details of the next line
        :raises StopIteration: If there are no more items
        """
  
    def check_victory(self) -> bool:
        """
        Check if the puzzle is in a victory state.
        
        Args:
            tubes (List[List[int]]): The grid representing tubes with colored balls.
        
        Returns:
            bool: True if the puzzle is solved, False otherwise.
        """
        # override this
        pass     
    
    def calc_move(self, source: int, destination: int) -> bool:
        """
        Calculate the move of colors from the source tube to the destination tube.

        :param source: The index of the source tube.
        :param destination: The index of the destination tube.
        :return: True if the move is successful, False otherwise.
        """
        # override this
        pass
    def next_grid_df(self) ->bool:
        # override this
        pass
    
    def initialize(self,*args, filePath=None, full=None, size=None, colors=None, empty=None):
        # override this
        pass
        
    def __call__(self) -> bool:
        """
        Solve the liquid puzzle.
        
        Args:
            stacksNumber (List[List[int]]): The initial state of the puzzle.
        
        Returns:
            List[List[int]]: List of moves to solve the puzzle.
        """
        # override this
        pass
