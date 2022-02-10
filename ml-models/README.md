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
export FLASK_APP=inference
export FLASK_ENV=development
export FLASK_RUN_PORT=5050
flask run
```