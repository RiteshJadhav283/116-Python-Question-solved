import logging
logging.basicConfig(level=logging.DEBUG,format='%(asctime)s-%(levelname)s-%(message)s')
logging.info("This is an info message.")
logging.error("This is an error message.")
try:
    x=10/0
except ZeroDivisionError as e:
    logging.error("An error occurred:%s",e,exc_info=True)