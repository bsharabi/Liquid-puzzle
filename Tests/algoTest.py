import unittest
from logic.Algo import Algo  # Adjust the import based on the actual location of your Algo class
from api.IAlgo import IAlgo
class TestAlgo(unittest.TestCase):
    """
    Test suite for the Algo class which includes tests for tube generation,
    puzzle solving, and various helper methods.
    """

    def setUp(self):
        """
        Set up the test environment before each test.
        """
        self.algo:IAlgo = Algo()

    def test_generate_tubes(self):
        """
        Test the generate_tubes method to ensure it creates tubes with the expected properties.
        """
        full = 2
        size = 4
        colors = 3
        empty_tube = 1

        tubes, unique_colors = self.algo.generate_tubes(full, size, colors, empty_tube)
        
        # Check the number of tubes
        self.assertEqual(len(tubes), size + empty_tube)
        
        # Check that each color appears the correct number of times
        color_counts = [0] * colors
        for tube in tubes:
            for ball in tube:
                color_counts[ball] += 1
        for count in color_counts:
            self.assertEqual(count, size)

        # Check that each tube has the same number of unique colors
        self.assertEqual(unique_colors, len(set(tubes[0])))

    def test_is_solved(self):
        """
        Test the is_solved method to check if it correctly identifies a solved puzzle.
        """
        grid = [[1, 1, 1], [2, 2, 2], [3, 3, 3], []]
        stack_height = 3
        self.assertTrue(self.algo.is_solved(grid, stack_height))

        grid = [[1, 1], [2, 2, 2], [3, 3, 3], [1]]
        self.assertFalse(self.algo.is_solved(grid, stack_height))

    def test_is_valid_move(self):
        """
        Test the is_valid_move method to ensure it correctly validates moves.
        """
        source_stack = [1, 1]
        destination_stack = [1]
        height = 3
        self.assertTrue(self.algo.is_valid_move(source_stack, destination_stack, height))

        source_stack = [1, 2]
        self.assertFalse(self.algo.is_valid_move(source_stack, destination_stack, height))

        destination_stack = [2]
        self.assertFalse(self.algo.is_valid_move(source_stack, destination_stack, height))

    def test_solve_puzzle(self):
        """
        Test the solve_puzzle method to ensure it can solve the puzzle correctly.
        """
        grid = [[1, 1], [2, 2], [3, 3], []]
        stack_height = 2
        visited = set()
        answer_mod = []
        memo = {}
        result = self.algo.solve_puzzle(grid, stack_height, visited, answer_mod, memo)
        self.assertTrue(result)

        grid = [[1, 2], [2, 1], [3, 3], []]
        visited = set()
        answer_mod = []
        memo = {}
        result = self.algo.solve_puzzle(grid, stack_height, visited, answer_mod, memo)
        self.assertFalse(result)

    def test_check_grid(self):
        """
        Test the check_grid method to ensure it correctly validates the grid.
        """
        grid = [[1, 1, 1], [2, 2, 2], [3, 3, 3], []]
        empty = 1
        self.assertTrue(self.algo.check_grid(grid, empty))

        grid = [[1, 1], [2, 2, 2], [3, 3, 3], [1]]
        self.assertFalse(self.algo.check_grid(grid, empty))

    def test_check_victory(self):
        """
        Test the check_victory method to ensure it correctly identifies a victory state.
        """
        tubes = [[1, 1, 1], [2, 2, 2], [3, 3, 3], []]
        self.algo.size = 3
        self.assertTrue(self.algo.check_victory(tubes))

        tubes = [[1, 1], [2, 2, 2], [3, 3, 3], [1]]
        self.assertFalse(self.algo.check_victory(tubes))

    def test_call(self):
        """
        Test the __call__ method to ensure it solves the puzzle and returns the correct moves.
        """
        stacksNumber = [[1, 1], [2, 2], [3, 3], []]
        result = self.algo(stacksNumber)
        self.assertEqual(result, [])

        stacksNumber = [[1, 2], [2, 1], [3, 3], []]
        result = self.algo(stacksNumber)
        self.assertTrue(len(result) > 0)

if __name__ == "__main__":
    unittest.main()
