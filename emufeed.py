#!/usr/bin/python
import iohandler
import sources

log = iohandler.Logger()
config = iohandler.Config(log)


def main():
    log.info("Reading configuration")
    config.read()
    log.set_debug_level(config.suppress_output, config.verbose)

    log.debug("Reading data")
    data = iohandler.Data(log)
    data.read()

    discord = iohandler.Discord(log, config.webhook_url)

    # import modules
    source_modules = []
    for c in config.sources:
        if hasattr(sources, c):
            source_modules.append(getattr(sources, c)(log, config))
        else:
            log.warn(f"Source module not found: {c}")

    # check for updates
    for source in source_modules:
        log.debug(f"Getting data for module {source.name}")
        title, description, link = source.get_latest()

        # if this is first run for module and no change
        module_name = type(source).__name__
        if module_name in data.data and data.data[module_name] == link:
            log.debug(f"No updates found for module {module_name}")
        else:
            discord.send(source, title, description, link)
            data.data[module_name] = link

    data.write()


if __name__ == "__main__":
    main()
