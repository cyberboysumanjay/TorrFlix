# TorrFlix
A simple torrent streamer written in python.
#### Tested on Linux 64bit system with Python 3.5

## How to use
TorrFlix uses Peerflix and Webtorrent as stream handler install any one or both as per your wish.
For that we need to setup nodejs and npm. 
#### Windows users can install nodejs from [here](https://nodejs.org/en/download/).
#### Linux users just fire up the terminal and run these commands.
> sudo apt-get update
> sudo apt-get install nodejs
> sudo apt-get install npm

This should install node.js and npm on your PC

Quickly check the installed version through this command. If this gave you an error you have to figure out how to install npm on your pc. Do a quick google search for a solution.

> nodejs -v

We're all set to install peerflix and webtorrent-cli now.
#### Linux users run this command. 
 
> sudo npm install -g peerflix 
> sudo npm install webtorrent-cli -g
#### Windows users can open Command Prompt and run these commands there. Don't forget to remove 'sudo' at the starting of the command. 

Make sure you have Python3 and pip installed on your pc, if not run this:
#### Linux users do this
> sudo apt-get install python3-pip
#### Windows users head over here and [download](https://www.python.org/downloads/) Python3 64bit 
Install all requirements at once using the command in linux:

> sudo -H pip3 install -r requirements.txt

Windows users just type:
> pip3 install -r requirements.txt

TorrFlix uses VLC for streaming. Make sure it is installed in your PC. Read install instructions [here](https://www.videolan.org/vlc/)

 It seems we are all set with the requirements things. Let's start the script now!
 Run the script using the command
 > python3 play.py   #Linux 
 > python play.py    #Windows
 
 Don't forget to star the repo if you like the work :)
 #### © Copyright  [Sumanjay](https://cyberboysumanjay.github.io)
 All rights reserved.
