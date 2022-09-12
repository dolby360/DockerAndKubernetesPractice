# Docker network


```bash
# To build each one of the images
docker build -t client-net client
docker build -t server-net server

# Then create a network
docker network create my-network
# Run server
docker run --rm -it --network my-network server-net
# Run client 
docker run --rm -it --network my-network client-net
```

