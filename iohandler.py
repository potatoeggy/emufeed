import configparser

class Logger:
    def __init__(self, suppress_output: bool = False, verbose: bool = False):
        self.suppress_output = suppress_output
        self.verbose = verbose

    def _log(self, msg, priority="DEBUG"):
        if not self.suppress_output:
            print(f"{priority}: {msg}")
    
    def debug(self, msg):
        if self.verbose:
            self._log(msg, "DEBUG")
    
    def info(self, msg):
        self._log(msg, "INFO")

    def warn(self, msg):
        self._log(msg, "WARN")
    
    def error(self, msg, abort: bool = False):
        self._log(msg, "ERROR")
        if abort:
            exit(1)
    
    def set_debug_level(self, suppress_output: bool = None, verbose: bool = None):
        if suppress_output is not None:
            self.suppress_output = suppress_output
        
        if verbose is not None:
            self.verbose = verbose


class Config:
    def __init__(self, log: Logger):
        self.log = log
        self.config = configparser.ConfigParser()
    
    def read(self):
        self.config.read("config.ini")
        return self.config

    def write(self):
        self.config.write("config.ini")

