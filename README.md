# LogMailer

Requires `msmtp` installed on a linux machine.

## Goal

The goal of this script is to send the log-files of the current day to a specified email address.

Not the log files from `/var/log/`, but only the ones from my scripts, which I store in `/home/myuser/cronjobs/logs/` on my ubuntu cloud server(s).

My log-files are named as follows: name of app, underscore, weekday (3 characters), and followed by `.log`.    
Example: `tweeps_SAT.log`. The next Saturday the log-file gets overwritten.

## msmtp

**msmtp** is a very simple and easy to use SMTP client with fairly complete sendmail compatibility.

To Do: adde installation and configuration information here.

## Code

### Configuration

In `config-sample.py` you will find the constants that the script needs to run on your server:

- the destination email address
- the location (absolute path) of the log directory

```python
DEST_EMAIL = "my.email@example.com"
LOG_DIR = "/home/myuser/cronjobs/logs/"
```

## Script

## Cron

I have configured `crontab` so that the script runs twice a day: at 10 past 11 am and 10 past 11 pm.

```bash
10 11,23 * * * python3 /home/j0h4n/cronjobs/logmailer/logmailer.py > /dev/null 2>&1
```

## To Do

Add logging to the script.