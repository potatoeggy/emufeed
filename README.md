# emufeed
A lightweight Python script to check for RSS feed updates and post them to a Discord channel as a webhook.

## Prerequisites

 - Python 3.6+
 - `feedparser` (`pip install feedparser`)
 - `requests` (`pip install requests`)

## Usage

1. Configure your wanted extra sources (if any) by adding their details in `sources.py` following the `Source` template.
2. Make a copy of `config.ini.sample` as `config.ini` in the same directory and toggle options you want to change.
  - `WebhookUrl`: the URL provided by Discord for webhooks. Can be obtained by navigating to a server > Edit Channel > Integrations > Webhooks > New webhook with the "Manage Channels" permission.
  - `Verbose`: show debug information if set to `True`. Defaults to `False`.
  - `Sources`: a comma-separated list of sources to enable in `sources.py` by their function name.
  - `Quiet`: suppress all output if set to `True`. Defaults to `False`.
  - `SendLatestOnFirstRun`: sends the latest post of all feeds on first run if set to `True`. Defaults to `False`.
3. Run the main script `emufeed.py`.

## Automatically starting emufeed

On Windows systems, Task Scheduler can be used to run emufeed at regular intervals.

On Linux systems, a sample systemd service and timer are provided (warning: no security options set by default) and they can be copied directly to `/etc/systemd/system/`.