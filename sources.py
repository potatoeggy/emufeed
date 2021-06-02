import configparser
import iohandler
import feedparser

class Source():
    def __init__(self, logger: iohandler.Logger, config: iohandler.Config):
        self.logger = logger
        self.config = config
    
    def get_latest(self):
        # override this function
        self.logger.error(f"{self.__class__.__name__} does not implement an update method.")
    
    def get_link_by_rss(self, link):
        entry = feedparser.parse(link)["entries"][0]
        return (entry.title, entry.link)


class yuzu(Source):
    name = "yuzu"
    def get_latest(self):
        return self.get_link_by_rss("https://yuzu-emu.org/index.xml")

class citra(Source):
    name = "Citra"
    def get_latest(self):
        return self.get_link_by_rss("https://citra-emu.org/index.xml")

class ryujinx(Source):
    name = "Ryujinx"
    def get_latest(self):
        return self.get_link_by_rss("https://blog.ryujinx.org/rss")

class dolphin(Source):
    name = "Dolphin"
    def get_latest(self):
        return self.get_link_by_rss("https://dolphin-emu.org/blog/feeds/")

class melonds(Source):
    name = "melonDS"
    def get_latest(self):
        return self.get_link_by_rss("http://melonds.kuribo64.net/rss.php")
