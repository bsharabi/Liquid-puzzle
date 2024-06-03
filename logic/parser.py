import csv
import os
import ast

root_dir = os.getcwd()
data_dir = os.path.join(root_dir, "data")
input_dir = os.path.join(data_dir, "inputs")
output_dir = os.path.join(data_dir, "outputs")

class Parser:
    """
    The Parser class handles reading from and writing to CSV files for puzzle data.
    It provides methods to read data line by line from an input CSV file and write data to an output CSV file.
    """
    
    def __init__(self, read_file_path: str = "example.csv", write_file_path: str = "example.csv") -> None:
        """
        Initializes the Parser object with file paths for reading and writing.

        :param read_file_path: Path to the input CSV file (default is "example.csv")
        :param write_file_path: Path to the output CSV file (default is "example.csv")
        """
        if not os.path.exists(data_dir):
            os.mkdir(data_dir)
        if not os.path.exists(input_dir):
            os.mkdir(data_dir)
        if not os.path.exists(output_dir):
            os.mkdir(data_dir)
            
        self.read_file_path = os.path.join(input_dir, read_file_path)
        self.write_file_path = os.path.join(output_dir, write_file_path)
        
    
    def reader(self,read_file_path) -> None:
        """
        Opens the input CSV file and initializes the CSV reader and iterator.
        """
        if self.read_file_path != os.path.join(input_dir, read_file_path):
            self.read_file_path = os.path.join(input_dir, read_file_path)
            if hasattr(self, '_read_file') and not self._read_file.closed:
                self._read_file.close()
            try:
                self._read_file = open(self.read_file_path, mode='r', newline='')
            except FileNotFoundError:
                raise FileNotFoundError(f"Input file not found: {self.read_file_path}")
            except Exception as e:
                raise Exception(f"An error occurred while opening the file: {e}")

            self._csv_reader = csv.DictReader(self._read_file)
            self._iterator = iter(self._csv_reader)

    def __del__(self):
        """
        Destructor to close the file when the object is deleted.
        """
        if hasattr(self, '_read_file') and not self._read_file.closed:
            self._read_file.close()

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

        item = self._next_item.copy()
        
        del self._next_item

        # Convert CSV row to the required dictionary format
        result = {
            "init": ast.literal_eval(item["init"]),  # Use ast.literal_eval for safety
            "empty": int(item["empty"]),
            "full": int(item["full"]),
            "size": int(item["size"]),
            "colors": int(item["colors"])
        }

        return result

    def writer(self, *arg,**data: dict) -> None:
        """
        Writes a dictionary to the output CSV file, appending a new line.

        :param data: A dictionary containing the data to write
        """
        if len(arg)!=0 and self.write_file_path !=os.path.join(output_dir, arg[0]):
            self.write_file_path=os.path.join(output_dir, arg[0])
        
        columns = list(data["data"].keys())
       
        # Ensure all required fields are present in the dictionary
        for column in columns:
            if column not in data["data"]:
                data["data"][column] = None  # or some default value

        file_exists = os.path.isfile(self.write_file_path)

        with open(self.write_file_path, mode='a', newline='') as write_file:
            dictwriter_object = csv.DictWriter(write_file, fieldnames=columns)
            
            # Write header only if file does not exist
            if not file_exists:
                dictwriter_object.writeheader()
            
            # Write the data row
            dictwriter_object.writerow(data["data"])


if __name__ == "__main__":
    try:
        # Create an instance of the Parser class
        parser = Parser('example.csv', 'output.csv')

        # Open the input file using the reader function
        parser.reader()

        # Read the CSV file
        while parser.hasNext():
            data = parser.next()
            print(data)

        # Write to the output CSV file
        parser.writer({
            "init": [[1, 3, 5, 4, 4, 7, 6, 1], [2, 2, 0, 0, 4, 3, 6, 7],
                     [2, 1, 1, 4, 5, 6, 0, 2], [0, 6, 6, 5, 4, 7, 7, 3],
                     [3, 4, 1, 0, 5, 7, 4, 4], [7, 6, 2, 2, 3, 1, 0, 0],
                     [7, 3, 3, 1, 2, 5, 5, 6], [7, 6, 5, 5, 3, 2, 1, 0], [], []],
            "empty": 2,
            "full": 8,
            "size": 8,
            "colors": 8,
            "stepToSolve": 5,
            "steps": ["step1", "step2", "step3", "step4", "step5"]
        })

    except Exception as e:
        print(f"An error occurred: {e}")
