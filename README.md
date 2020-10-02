# LunchBot

###This project was an educational exercise for Fullstack Academy's Cyber Security Bootcamp.

##Contents

1. README.md
    You're here now.
2. GUI.py
    Running this both starts a python server on port 8080 and launches a graphic user interface to issue commands to "victim" machines.  Inputting the UID of a specific machine will instruct that machine.  Inputting `any` for the UID will instruct all active machines.
3. Instructions_editor.py
    Python script that the GUI calls to edit a file hosted on the server called `instructions.txt`.
4. ServerStart.py
    Python script that the GUI calls to launch the server.  This script also sets up a directory called `server` and pupulates them with the files `botnames.txt`, `logs.txt`, and `instructions.txt`.
5. editbotname.py
    ServerStart.py calls this script to maintain a roster of machines listed on `botnames.txt`.  The script updates the list as machines send a POST request to the server with their UID.
6. EasyBot.py
    This script reads the crontab and adds two cronjobs (if they aren't already present) that ensure that this script is ran every day at noon and that a function called `instructions()` is ran every minute.  It then creates a directory called `.bot` in the `/tmp` directory if it doesn't already exist.
    A file called `name.txt` is written to the `.bot` directory.  The script checks the page `botnames.txt` and assigns itself a UID based on the last listed integer on the page.  For example if the last integer is 5, then the script will write 6 into the `name.txt` file.
    The `instructions()` function sends a GET request to `instructions.txt`.  If the machine finds instructions with `any` or its UID on the page, it will execute those instructions and send a time stamped output with its UID to the server.  If there are no instructions for the machine, then it will send a time-stamped message to the logs saying that it is online.  All GET and POST requests are documented on the serverside in `logs.txt`.
<dl>

##Notes:  In the GUI, the stop server button kills <b>all</b> running python processes on the host machine.
          In lunchbox.py, replace the `{IP}` tag where it is present with the IP address of the machine hosting the server.



**© 2020 Alex Harris and Charles Timmons**
  *This is for educational purposes only.  Feel free to test this on your own network, but we do not condone this being used for any unauthorized or illegal activites.*
