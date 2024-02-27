import csv
import logging

logging.basicConfig(level=logging.INFO)

'''
Description: Class to interface with the output csv file.
'''
class CSVOutputAdapter:
    def __init__(self, config):
        self.config = config
    
    def write_output(self, data, file_path):
        success = True
        try:
            with open(file_path, "w", newline="") as output:
                writer = csv.DictWriter(output, fieldnames=self.config["output_columns"])
                writer.writeheader()
                for row in data:
                    writer.writerow(row)
        except Exception as ex:
            logging.error("Error when writing to file: %s", ex)
            success = False
        return success
        
