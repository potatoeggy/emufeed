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

class Config:
    pass