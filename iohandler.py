import configparser
import json
from typing import Final
import feedparser
from feedparser.util import FeedParserDict
import requests


class Logger:
    def __init__(self, suppress_output: bool = False, verbose: bool = False):
        self.suppress_output = suppress_output
        self.verbose = verbose

    def _log(self, msg: str, priority: str = "DEBUG"):
        if not self.suppress_output:
            print(f"{priority}: {msg}")

    def debug(self, msg: str):
        if self.verbose:
            self._log(msg, "DEBUG")

    def info(self, msg: str):
        self._log(msg, "INFO")

    def warn(self, msg: str):
        self._log(msg, "WARN")

    def error(self, msg: str, abort: bool = False):
        self._log(msg, "ERROR")
        if abort:
            exit(1)

    def set_debug_level(self, suppress_output: bool = None, verbose: bool = None):
        if suppress_output is not None:
            self.suppress_output = suppress_output

        if verbose is not None:
            self.verbose = verbose


class Config:
    __slots__ = ["log", "config", "webhook_url", "verbose",
                 "suppress_output", "sources", "ignore_if_empty_json"]

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
        self.ignore_if_empty_json = not general.getboolean(
            "SendLatestOnFirstRun", fallback=False
        )


class Data:
    def __init__(self, log: Logger):
        self.data: dict = {}
        self.log: Final = log

    def read(self):
        try:
            with open("data.json", "r") as file:
                self.data: dict = json.loads(file.read())
        except FileNotFoundError:
            # expected, will be created later
            pass

    def write(self):
        with open("data.json", "w") as file:
            file.write(json.dumps(self.data))


class Source:
    name: str = "Source Name"
    url: str = "Source Home URL"
    logo: str = None

    def __init__(self, log: Logger, config: Config):
        self.log: Final[Logger] = log
        self.config: Final[Config] = config

    def get_latest(self):
        # override this function, return three strings: title, description, and link
        self.log.error(
            f"{self.__class__.__name__} does not implement an update method."
        )

    def get_link_by_rss(self, link: str) -> tuple[str, str, str]:
        entry: Final[FeedParserDict] = feedparser.parse(link)["entries"][0]
        return (entry.title, entry.description, entry.link)


class Discord:
    def __init__(self, log: Logger, webhook_url: str):
        self.log: Final = log
        self.webhook_url: Final = webhook_url

    def send(self, source: Source, title: str, description: str, link: str):
        payload: dict = {
            "username": source.name,
            "avatar_url": source.logo,
            "content": f"[{title}]({link})",
        }
        if source.logo:
            payload["avatar_url"] = source.logo
        requests.post(self.webhook_url, data=payload)
