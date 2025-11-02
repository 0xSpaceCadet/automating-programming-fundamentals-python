import logging as logging
logging.basicConfig(level=logging.DEBUG, format=' %(asctime)s -  %(levelname)s -  %(message)s')

logging.debug("Debug message")
logging.info("Something happened")
logging.warning("Potential issue")
logging.error("Something went wrong")
logging.critical("System failure")

# while looping from reosurce we should always have a STATE machine
# that keeps track of what has happened and what has NOT

