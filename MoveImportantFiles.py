import os
import shutil
import logging
from datetime import datetime

# Set up logging
log_folder = os.path.dirname(os.path.abspath(__file__))
log_file = os.path.join(log_folder, 'file_moves.log')
logging.basicConfig(
    filename=log_file,
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

# Define source and destination folders
source_folder = os.path.expanduser("YOUR_DOWNLOADS_FOLDER_PATH")
destination_folder = "YOUR_DESTINATION_FOLDER_PATH"

try:
    # Loop through files in the source folder
    for filename in os.listdir(source_folder):
        # Check if the file starts with 'importantName' and has a .pdf extension
        if filename.startswith("ImportantNameStart") and filename.endswith(".pdf"):
            # Get the full file paths
            source_file = os.path.join(source_folder, filename)
            destination_file = os.path.join(destination_folder, filename)
            
            try:
                # Move the file
                shutil.move(source_file, destination_file)
                logging.info(f"Successfully moved file: {filename}")
                print(f"Moved: {filename}")
            except Exception as e:
                logging.error(f"Error moving file {filename}: {str(e)}")
                print(f"Error moving {filename}: {str(e)}")

except Exception as e:
    logging.error(f"Script error: {str(e)}")
    print(f"Script error: {str(e)}")