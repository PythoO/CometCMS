import logging


class CometLog:
    def __init__(self):
        logging.basicConfig(filename='comet.log', level=logging.DEBUG)

    def debug(self, msg):
        logging.debug('%s' % msg)

    def info(self, msg):
        logging.info('%s' % msg)

    def warning(self, msg):
        logging.warning('%s' % msg)