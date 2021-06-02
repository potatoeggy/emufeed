import configparser
import json
import requests

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
        
        general = self.config["emufeed"]
        self.webhook_url = general.get("WebhookUrl")
        self.verbose = general.getboolean("Verbose", fallback=False)
        self.suppress_output = general.getboolean("Quiet", fallback=False)
        self.sources = general.get("Sources").split(",")


class Data:
    def __init__(self, log: Logger):
        self.data = {}
        self.log = log

    def read(self):
        try:
            with open("data.json", "r") as file:
                self.data = json.loads(file.read())
        except FileNotFoundError:
            # expected, will be created later
            pass

    def write(self):
        with open("data.json", "w") as file:
            file.write(json.dumps(self.data))

class Discord:
    def __init__(self, log: Logger, webhook_url):
        self.log = log
        self.webhook_url = webhook_url
    
    def send(self, source, title, description, link):
        payload = {
            "username": source.name,
            "avatar_url": source.logo,
            "content": f"[{title}]({link})"
        }
        requests.post(self.webhook_url, data=payload)