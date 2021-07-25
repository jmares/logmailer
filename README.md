# LogMailer

Requires `msmtp` installed on a linux machine.

## Goal

The goal of this script is to send the log-files of the current day to a specified email address.

Not all the log files from `/var/log/`, but only the ones from my scripts, which I store in `/home/myuser/cronjobs/logs/` on my ubuntu virtual private server(s).

My log-files are named as follows: name of app, underscore, weekday, and .log extension. Example: `tweeps_SAT.log`