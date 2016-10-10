HTTP Media Server for VLC
=========================

Me and my friends needed to watch movies and listen to songs wirelessly from a desktop which had all the hard disks attached to it. SMB, AFP were too much of a hassle to set up and not to mention slow, jittery performance. I am looking at you Mac OS. ( SMB 1 in 2016 ?) Hence the python script.

Shows vlc playlist directly in vlc. So that you can click and play :). Both random and incremental seek in vlc is supported. Playing directly in the browser is supported too.

Has no dependencies other than python standard libary. Have fun!


Installation
------------
Not required as there are no dependencies. :)


Usage
-----
video.py [-h] [--directory DIRECTORY] [--port PORT] [--foreground]
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

