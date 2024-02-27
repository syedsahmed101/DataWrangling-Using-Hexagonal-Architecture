import csv
import sys
import logging

logging.basicConfig(level=logging.INFO)

'''
Description: Class to interface with the input csv file.
'''
class CSVInputAdapter:
    def read_input(self, file_path):
        input_data = []
        try:
            with open(file_path, "r") as input:
                reader = csv.DictReader(input)
                for row in reader:
                    input_data.append(row)
        except FileNotFoundError as fex:
            logging.error("Input csv file not found error occurred: %s", fex)
            input_data = None
        except Exception as ex:
            logging.error("Error occurred with reading the csv file: %s", ex)
            sys.exit(1)
        if len(input_data) == 0:
            input_data = None
        return input_data