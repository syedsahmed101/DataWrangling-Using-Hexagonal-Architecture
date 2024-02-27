from application.data_wrangling_service import ApplicationService
import logging

logging.basicConfig(level = logging.INFO)

def main():
    input_file = 'input.csv'
    output_file = 'output.csv'
    config_file = 'application/config.json'
    
    app_service = ApplicationService(config_file)
    is_success = app_service.process_data(input_file, output_file)
    if is_success:
        logging.info("Data successfully written.")
    else:
        logging.info("Failed to write data. Check errors and try again.")

if __name__ == "__main__":
    main()
