# Bund API

This API should bring easy access to data, which is sometimes really interesting, but not really easy accessible.

Currently it is in development and only the wasserpegel api is working.

Run
```
python pip install -r requirements.txt
gunicorn -k uvicorn.workers.UvicornWorker main:app --bind=0.0.0.0
```

## Autobahn api
This part of the api is currently not implemented, but it will be able to view current statuses of the autobahn

## Wasserpegel
Wasserpegel api is able to view the latest waterlevels of selected rivers at selected stations.
In the future, this will be for all rivers in Germany and dynamic, currently it is statically implemented.

## TODO's
- [ ] Wasserpegel für alle in Sachsen verfügbaren Messstellen
- [ ] Erweiterung auf benachbarte Länder von Sachsen
