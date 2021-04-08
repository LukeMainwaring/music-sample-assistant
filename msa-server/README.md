Docker scripts to run:
\$ docker-compose up

If image needs to be rebuilt
\$ docker-compose up --build

To stop:
Ctrl + c,
\$ docker-compose down

This link was super helpful in getting started: https://docs.docker.com/compose/gettingstarted/


Local run:
\$ export FLASK_APP=app.py
\$ export FLASK_ENV=development
\$ flask run