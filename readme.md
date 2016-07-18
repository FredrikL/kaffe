Kaffe
===

Script for a Slack [python-rtmbot](https://github.com/slackhq/python-rtmbot) that listens for a command ("finns det kaffe") then takes a photo and sends it to slack.

Parts needed
==
raspberry pi (only tested on a pi1 b+)  
raspberry pi camera  
slack bot [integration](https://api.slack.com/bot-users) 

Installation
==

* Activate the camera module on the pi
* `pip install boto python-picamera`
* [Configure](http://docs.pythonboto.org/en/latest/boto_config_tut.html) boto
* Install python-rtmbot
* Add slack token to rtmbot.conf
* Copy kaffe.py to plugins
* Start the bot `./rtmbot.py`





