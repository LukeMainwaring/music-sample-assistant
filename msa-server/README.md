Docker scripts to run:

```bash
docker-compose up
docker-compose up --build # If image needs to be rebuilt
```

To stop:
```bash
Ctrl + c
docker-compose down
```

Local run:

```bash
export FLASK_APP=app
export FLASK_ENV=development
flask run
```