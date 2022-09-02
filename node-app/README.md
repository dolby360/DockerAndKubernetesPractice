# Docker example for node app

```bash
# docker build
docker build -t node_example:delete_me .
```

```bash
# docker run detached, expose port, delete after finish and give name
docker run --name delteme -d --rm -p 3000:3000 node_example:delete_me
```

