# Match Data Web-Scraper

A simple script that Web-Scrapes the data from the last match played by a team.

# Setup

Firstly, create a "config.txt" file in the root folder and paste your User Agent inside of it (this is found by searching "what is my user agent?").

Secondly, enter the included virtual environment:
```
source ./venv/bin/activate
```

Congratulations! Everything is set up. You can now run the script via inclding "scraper.py" in another file and accessing the matchStats(team) function, or you can run it as a server (make sure to read bellow for more information if using as server).

IF YOU ARE USING THIS AS A SERVER USE THIS COMMAND TO START IT:
```
uvicorn server:app
```
