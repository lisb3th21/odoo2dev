# odoo2dev
Docker Odoo 10 to developer 

```
docker compose up -d
docker compose up -d --build
```

```
docker compose down
```

```
http://localhost:8010/web/database/selector
```


# Odoo 10
```
$ docker run -d -e POSTGRES_USER=odoo -e POSTGRES_PASSWORD=odoo -e POSTGRES_DB=postgres --name db postgres:13
$ docker run -p 8069:8069 --name odoomfh10 --link db:db -t mfalconsoft/odoo:10.0
```

