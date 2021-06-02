#!/usr/bin/python
import iohandler
import sources

log = iohandler.Logger()
config = iohandler.Config(log)

def main():
    config.read()
    log.set_debug_level(config.suppress_output, config.verbose)

if __name__ == "__main__":
    main()
