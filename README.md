# TorrFlix :movie_camera:
A simple torrent streamer written in Python 3.
#### Tested on Linux 64bit system with Python 3.8.2

## How to use
TorrFlix uses Webtorrent-CLI as stream handler.
For that we need to setup nodejs and npm.
#### Windows users can install nodejs from [here](https://nodejs.org/en/download/).
#### Linux users just fire up the terminal and run these commands.
> sudo apt-get update

> sudo apt-get install nodejs

> sudo apt-get install npm

This should install node.js and npm on your PC

Quickly check the installed version through this command. If this gave you an error you have to figure out how to install npm on your pc. Do a quick google search for a solution.

> nodejs -v

We're all set to install webtorrent-cli now.
#### Linux users run this command.

> sudo npm install webtorrent-cli -g

#### Windows users can open Command Prompt and run these commands there. Don't forget to remove 'sudo' at the starting of the command.

Make sure you have Python3 and pip installed on your pc, if not run this:
#### Linux users do this
> sudo apt-get install python3-pip
#### Windows users head over here and [download](https://www.python.org/downloads/) Python3 64bit

Install all requirements at once using the command:

> pip3 install -r requirements.txt


TorrFlix suggests VLC for streaming. Make sure it is installed in your PC. Read install instructions [here](https://www.videolan.org/vlc/)

 Let's start the script now!
 Run the script using the command
 > python3 play.py   

 Don't forget to star the repo if you like the work :)
 #### © Copyright  [Sumanjay](https://cyberboysumanjay.github.io)
 All rights reserved.
