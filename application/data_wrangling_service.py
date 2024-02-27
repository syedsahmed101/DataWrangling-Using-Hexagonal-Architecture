from core.services import WranglingService
from adapters.input_adapter import CSVInputAdapter
from adapters.output_adapter import CSVOutputAdapter
from adapters.configuration_adapter import ConfigurationAdapter
import json
import logging

logging.basicConfig(level=logging.INFO)

class ApplicationService:
    def __init__(self, config_file):
        self.config_adapter = ConfigurationAdapter(config_file)
        self.config = self.config_adapter.load_configuration()
        self.input_adapter = CSVInputAdapter()
        self.output_adapter = CSVOutputAdapter(self.config)
        self.wrangle_service = WranglingService(self.config)


    def process_data(self, input_file, output_file):
        success = True

        # Read CSV data
        input_data = self.input_adapter.read_input(input_file)
        
        if input_data:
            # Transforming data if input data available
            transformed_data = self.wrangle_service.transform_data(input_data)
            
            if transformed_data:
                # Writing the data to a CSV file if the data successfully transformed.
                success = self.output_adapter.write_output(transformed_data, output_file)
            else:
                success = False
        else:
            success = False
        return success