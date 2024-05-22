import unittest
import os
import csv
from logic.parser import Parser  # Adjust the import based on the actual location of your Parser class

class TestParser(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        # Create necessary directories if they don't exist
        cls.data_dir = os.path.join(os.getcwd(), "data")
        cls.input_dir = os.path.join(cls.data_dir, "inputs")
        cls.output_dir = os.path.join(cls.data_dir, "outputs")
        
        os.makedirs(cls.input_dir, exist_ok=True)
        os.makedirs(cls.output_dir, exist_ok=True)

        # Create a sample input CSV file
        cls.sample_input_path = os.path.join(cls.input_dir, "test_input.csv")
        with open(cls.sample_input_path, mode='w', newline='') as file:
            writer = csv.DictWriter(file, fieldnames=["init", "empty", "full", "size", "colors"])
            writer.writeheader()
            writer.writerow({
                "init": "[[1, 2], [3, 4]]",
                "empty": "2",
                "full": "2",
                "size": "4",
                "colors": "2"
            })
        
        cls.sample_output_path = os.path.join(cls.output_dir, "test_output.csv")

    @classmethod
    def tearDownClass(cls):
        # Clean up the created files and directories
        if os.path.exists(cls.sample_input_path):
            os.remove(cls.sample_input_path)
        if os.path.exists(cls.sample_output_path):
            os.remove(cls.sample_output_path)
        os.rmdir(cls.input_dir)
        os.rmdir(cls.output_dir)
        os.rmdir(cls.data_dir)

    def setUp(self):
        # Initialize the parser object for each test
        self.parser = Parser('test_input.csv', 'test_output.csv')

    def test_reader(self):
        # Test the reader method
        self.parser.reader()
        self.assertTrue(hasattr(self.parser, '_read_file'))
        self.assertTrue(hasattr(self.parser, '_csv_reader'))
        self.assertTrue(hasattr(self.parser, '_iterator'))

    def test_hasNext_and_next(self):
        # Test hasNext and next methods
        self.parser.reader()
        self.assertTrue(self.parser.hasNext())
        data = self.parser.next()
        expected_data = {
            "init": [[1, 2], [3, 4]],
            "empty": 2,
            "full": 2,
            "size": 4,
            "colors": 2
        }
        self.assertEqual(data, expected_data)
        self.assertFalse(self.parser.hasNext())

    def test_init_dict(self):
        # Test the init_dict method
        init = [[1, 2], [3, 4]]
        empty = 2
        full = 2
        size = 4
        colors = 2
        num_step = 5
        steps = ["step1", "step2"]
        time = 100

        expected_dict = {
            "init": init,
            "empty": empty,
            "full": full,
            "size": size,
            "colors": colors,
            "stepToSolve": num_step,
            "steps": steps,
            "timetoSolve": time
        }
        result_dict = self.parser.init_dict(init, empty, full, size, colors, num_step, steps, time)
        self.assertEqual(result_dict, expected_dict)

    def test_writer(self):
        # Test the writer method
        data = {
            "init": [[1, 3, 5], [2, 4, 6], [1, 2, 3], [4, 5, 6]],
            "empty": 1,
            "full": 3,
            "size": 3,
            "colors": 3,
            "stepToSolve": 5,
            "steps": ["step1", "step2", "step3", "step4", "step5"],
            "timetoSolve": 120
        }
        self.parser.writer(data)
        
        # Check if the file is created
        self.assertTrue(os.path.exists(self.sample_output_path))
        
        # Check the content of the file
        with open(self.sample_output_path, mode='r', newline='') as file:
            reader = csv.DictReader(file)
            rows = list(reader)
            self.assertEqual(len(rows), 1)
            row = rows[0]
            self.assertEqual(row["init"], str(data["init"]))
            self.assertEqual(row["empty"], str(data["empty"]))
            self.assertEqual(row["full"], str(data["full"]))
            self.assertEqual(row["size"], str(data["size"]))
            self.assertEqual(row["colors"], str(data["colors"]))
            self.assertEqual(row["stepToSolve"], str(data["stepToSolve"]))
            self.assertEqual(row["steps"], str(data["steps"]))
            self.assertEqual(row["timetoSolve"], str(data["timetoSolve"]))

if __name__ == "__main__":
    unittest.main()
