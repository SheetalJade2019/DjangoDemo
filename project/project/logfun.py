# importing module
import logging
from project.settings import BASE_DIR

# Create and configure logger
logging.basicConfig(filename=f"{BASE_DIR}/django.log",
					format='%(asctime)s %(message)s',
					filemode='a+')

# Creating an object
logger = logging.getLogger()

# Setting the threshold of logger to DEBUG
logger.setLevel(logging.DEBUG)

# Test messages
# logger.debug("Harmless debug Message")
# logger.info("Just an information")
# logger.warning("Its a Warning")
# logger.error("Did you try to divide by zero")
# logger.critical("Internet is down")
