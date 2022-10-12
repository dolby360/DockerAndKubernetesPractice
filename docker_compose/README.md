# Docker compose example
In this example, I set a client backend and database.
The client is sending a message to backend and backend prints the database content.
The database uses volume to store saved data and keep data persist between runs.

```bash
# In one shell
docker-compose up --build -d && docker attach client 
# Then press enter
```

```bash
# In other shell
docker attach backend
# To see logs
```
