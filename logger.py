import json_logging, logging, sys

class CustomLogger:
    def __init__(self):
        # log is initialized without a web framework name
        json_logging.ENABLE_JSON_LOGGING = True
        json_logging.init_non_web()

    def initlogger(self):
        logger = logging.getLogger("recon-svc-logger")
        if not logger.handlers:
            logger.setLevel(logging.INFO)
            logger.addHandler(logging.StreamHandler(sys.stdout))

        return logger
