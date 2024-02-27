import unittest
from unittest.mock import MagicMock
from core.services import WranglingService

class TestInputDataColumns(unittest.TestCase):
    def setUp(self):
        self.configuration_file = {"input_columns": ["Order Number", "Year", "Month", "Day", "Product"],}
        self.input_data = [{"Order Number": "1", "Year": "2024", "Month": "01", "Day": "01", "Product": "xyz"}]
        self.wrangling_service = WranglingService(self.configuration_file)

    '''
    This test will pass because the expected columns (self.configuration_file) and 
    actual columns (self.input_data) match
    '''
    def test_if_input_data_column_expected(self):
        output = self.wrangling_service.validate_input_columns(self.input_data)    
        assert output == True

if __name__ == "__main__":
    unittest.main()