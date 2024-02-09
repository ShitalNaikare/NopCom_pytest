import logging
import inspect

class LoggenClass:

    @staticmethod
    def log_generator():
        log_name = inspect.stack()[1][3]
        logger = logging.getLogger(log_name)
        logfile = logging.FileHandler("C:\\Users\\Admin\\PycharmProjects\\nopcom_pytest\\Logs\\NopCom_Logs.log")
        log_format = logging.Formatter(
            "%(asctime)s : %(levelname)s : %(name)s : %(funcName)s : %(lineno)s : %(message)s ")
        logfile.setFormatter(log_format)  # setting format to the logs
        logger.addHandler(logfile)  # adding log everytime to same file
        logger.setLevel(logging.INFO)  # set log level
        return logger
