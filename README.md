HTTP Media Server for VLC
=========================

We ( actually I and some of my friends ) needed to watch movies and listen to songs wirelessly from a desktop which has all the hard disks attached to it. SMB, AFP, etc were too much of a hassle to set up and not to mention slow, jittery performance. I am looking at you Mac OS ( SMB 1 in 2016 ?). Hence the python script.

Shows the playlist directly in vlc. So that you can click and play :). Both random and incremental seek in vlc is supported. Playing directly in the browser is supported too.

Requires `netifaces` other than python standard libary. Have fun!

PyPi repsitory - [videopy](https://pypi.python.org/pypi/videopy/0.0.1)

Installation
------------
pip install videopy


Usage
-----
videopy [-h] [--directory DIRECTORY] [--port PORT] [--foreground]
                [--stop] [--restart] [--pid PID]


optional arguments:

  -h, --help            show this help message and exit

  --directory DIRECTORY, -d DIRECTORY
                        Directory where the media is located

  --port PORT, -p PORT  Port the Media Server will bind to

  --foreground, -f      Start the Media Server in the foreground

  --stop                Stop the Media Server.

  --restart             Restart the Media Server

  --pid PID             Location to store the pid file


Watch
------
Just run `vlc http://[ip-address of the machine running the service]:[1149 or the port the service is running at]/vlc`

To play on a html5 enabled browser use `http://[ip-address of the machine running the service]:[1149 or the port the service is running at]`


Misc
----
Hope it helps you as much as it's helping us. 

Issues and Pull Requests are welcome.

But most importantly have fun.
