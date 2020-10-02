# LunchBot

The project was an educational exercise in 

This package contains both a Python executable that adds a Linux device to a botnet.  We also built a bot command server controlled by a GUI.

The GUI starts the server and sets up a directory that hosts the files necessary for its own operation and the operation of its bots.  The server posts the files on a webpage to allow easy communication and monitoring of all trafic.  The GUI allows the user to easily issue custom commands to the bots as a group or individually.  The server also maintains a roster of all the devices that have become part of the network so that new devices are able to name themselves.

The victim side executable automatically creates a hidden directory for itself to work out of and edits the crontab.  The first time it is launched, it assigns itself a UID and sends that information to the server by comparing against previously assigned names hosted on the website.  It regularly checks to see if the server has commands for it by parsing the instructions page on the website for commands assigned to its UID.  When it has a command to run, it executes it on the command line and sends the output to the server log in a timestamped readable format.  If there are no commands, it sends a message to the server announcing that it is online.  The executable is written in such a way that no matter where it lives in the device, it will still function properly.

##Note:  In the GUI, the stop server button kills <b>all</b> running python processes.
