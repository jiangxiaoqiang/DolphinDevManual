#coding=utf-8
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

#Create a file handler
handler = logging.FileHandler('output.log')
handler.setLevel(logging.INFO)

#Create a logging format
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
handler.setFormatter(formatter)

# add the handlers to the logger
logger.addHandler(handler)

def loginfo():
    logger.info('info')
    return

