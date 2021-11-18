import configparser

from iohandler import Source
import iohandler
import feedparser


class yuzu(Source):
    name = "yuzu"
    url = "https://yuzu-emu.org"
    logo = "https://avatars.githubusercontent.com/u/35075882?s=200&v=4"

    def get_latest(self):
        return self.get_link_by_rss("https://yuzu-emu.org/index.xml")


class citra(Source):
    name = "Citra"
    url = "https://citra-emu.org"
    logo = "https://raw.githubusercontent.com/citra-emu/citra/master/dist/icon.png"

    def get_latest(self):
        return self.get_link_by_rss("https://citra-emu.org/index.xml")


class ryujinx(Source):
    name = "Ryujinx"
    url = "https://ryujinx.org"
    logo = "https://raw.githubusercontent.com/Ryujinx/Ryujinx/master/Ryujinx/Ui/Resources/Logo_Ryujinx.png"

    def get_latest(self):
        return self.get_link_by_rss("https://blog.ryujinx.org/rss")


class dolphin(Source):
    name = "Dolphin"
    url = "https://dolphin-emu.org"
    logo = "https://raw.githubusercontent.com/dolphin-emu/dolphin/master/Data/dolphin-emu.png"

    def get_latest(self):
        return self.get_link_by_rss("https://dolphin-emu.org/blog/feeds/")


class melonds(Source):
    name = "melonDS"
    url = "http://melonds.kuribo64.net"
    logo = "https://raw.githubusercontent.com/StapleButter/melonDS/master/icon/melon_128x128.png"

    def get_latest(self):
        return self.get_link_by_rss("http://melonds.kuribo64.net/rss.php")


class asahi_linux(Source):
    name = "Asahi Linux"
    url = "https://asahilinux.org/"
    logo = "https://raw.githubusercontent.com/AsahiLinux/artwork/main/logos/png_128/AsahiLinux_logomark.png"

    def get_latest(self):
        return self.get_link_by_rss("https://asahilinux.org/blog/index.xml")


class supergoodcode(Source):
    name = "Mike Blumenkrantz"
    url = "https://www.supergoodcode.com"

    def get_latest(self):
        return self.get_link_by_rss("https://www.supergoodcode.com/feed.xml")


class asus_linux(Source):
    name = "ASUS Linux"
    url = "https://asus-linux.org/blog"

    def get_latest(self):
        return self.get_link_by_rss("https://asus-linux.org/rss.xml")
