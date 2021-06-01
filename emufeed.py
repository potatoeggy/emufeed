#!/usr/bin/python
import iohandler

log = iohandler.Logger()
config = iohandler.Config(log)

def main():
    config.read()

if __name__ == "__main__":
    main()
