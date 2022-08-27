# Volume Example

```shell
# Build the docker image
docker build -t docker_course_volume_example .
# Run container with volume and path /vol 
docker run -it -v test:/app docker_course_volume_example
# To map the volume to current dir
docker run -it -v $(pwd):/app  docker_course_volume_example
# The command above will override the node module directory, to overcome this issue
# we need to mount the node_modules as well (even if not exist locally).
docker run -it -v $(pwd):/app -v /app/node_modules  docker_course_volume_example
```
