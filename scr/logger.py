import os
from datetime import datetime
import logging

# Define log directory
LOG_DIR = os.path.join(os.getcwd(), "logs")

# Ensure the log directory exists
os.makedirs(LOG_DIR, exist_ok=True)

# Generate log file name with timestamp
LOG_FILE = f"{datetime.now().strftime('%Y-%m-%d_%H-%M-%S')}.log"
LOG_FILE_PATH = os.path.join(LOG_DIR, LOG_FILE)

# Print log file path for debugging
print(f"Log directory: {LOG_DIR}")
print(f"Expected log file path: {LOG_FILE_PATH}")

# Configure logging
logging.basicConfig(
    filename=LOG_FILE_PATH,
    format='[%(asctime)s] %(levelname)s - %(message)s',
    level=logging.INFO
)

if __name__ == "__main__":
    # Test logging
    logging.info("Logging system initialized.")
    # logging.info("This is a test log message.")
    # logging.error("This is a test error message.")
    # logging.warning("This is a test warning message."
    # logging.debug("This is a test debug message.")
# logging.info("Logging system initialized.")
# print("✅ Log message written successfully!")
# except Exception as e:
#     print(f"❌ Failed to write log message: {e}")