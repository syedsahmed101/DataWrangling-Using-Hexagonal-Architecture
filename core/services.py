from core.entities import Order
from datetime import datetime
from decimal import Decimal
import sys
import logging

logging.basicConfig(level=logging.INFO)

class WranglingService:
    def __init__(self, config):
        self.config = config
        
        # Will be used to log invalid rows.
        self.invalid_rows = []
        
        # Will be used in validation of the input columns with the expected columns.
        self.missing_columns = []

    def convert_data_type(self, val, type):
        if type == "String":
            val = str(val)
        elif type == "Integer":
            val = int(val)
        elif type == "DateTime":
            val = datetime.strptime(val, "%Y%m%d")
        elif type == "BigDecimal":
            val = Decimal(val.replace(",", ""))
        return val        

    '''
    Description: Transformations applied to the columns based on the transformation configuration file.
    '''
    def transform_row(self, row):
        transformed_row = {}

        try:
            for transform in self.config['transformations']:
                if 'rename' in transform:
                    original_column = transform['rename']['from']
                    new_column = transform['rename']['to']
                    type = transform['rename']['type']
                    if original_column in row:
                        transformed_row[new_column] = self.convert_data_type(row[original_column], type)

                if 'concatenate' in transform:
                    new_column = transform['concatenate']['to']
                    columns_to_concat = transform['concatenate']['columns']
                    type = transform['concatenate']['type']
                    concatenated_value = ''.join([row[col] for col in columns_to_concat])
                    transformed_row[new_column] = self.convert_data_type(concatenated_value, type)

                if 'add_column' in transform:
                    new_column = transform['add_column']['name']
                    value = transform['add_column']['value']
                    type = transform['add_column']['type']
                    transformed_row[new_column] = self.convert_data_type(value, type)
        except ValueError as ve:
            self.invalid_rows.append(row)
            logging.error("Error transforming the row: %s", row)
        except Exception as ex:
            logging.error("Error occurreed in service/transform_row(): %s", ex)
            transformed_row = {} 

        return transformed_row        
        
    def transform_data(self, data):
        transformed_data = []
        
        is_valid_input_columns = self.validate_input_columns(data)
        if not is_valid_input_columns:
            logging.error("The input data columns are not supported. Fix the column names and try again.")
            return transformed_data

        for row in data:
            transformed_row = self.transform_row(row)
            if transformed_row:
                transformed_data.append(transformed_row)

        if self.invalid_rows:
            logging.error("Invalid rows found: %s", self.invalid_rows)    
        
        return transformed_data
    
    ''''
    Description: Used to validate the columns in the input csv with the expected input columns in the 
    transformation configuration file.
    '''
    def validate_input_columns(self, data):
        expected_columns = self.config["input_columns"]
        actual_columns = []
        for row in data:
            for k in row:
                actual_columns.append(k)
            for col in expected_columns:
                if col not in actual_columns:
                    logging.error("The input data column %s is missing.", col)
                    self.missing_columns.append(col)

        if len(self.missing_columns) > 0:
            return False
        else:
            return True
      
