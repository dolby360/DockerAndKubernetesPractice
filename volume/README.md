# Volume Example

```bash
# Build the docker image
docker build -t docker_course_volume_example .

# Run with configured arguments --build-arg
docker build -t docker_course_volume_example --build-arg MY_ARG=90 .

# Run container with volume and path /vol 
docker run -it -v test:/app docker_course_volume_example

# To map the volume to current dir
docker run -it -v $(pwd):/app  docker_course_volume_example

# The command above will override the node module directory, to overcome this issue
# we need to mount the node_modules as well (even if not exist locally).
docker run -it -v $(pwd):/app -v /app/node_modules  docker_course_volume_example

# Use a file with environment variables
docker run --rm  -d -v $(pwd):/app -v /app/node_modules --env-file .env docker_course_volume_example
```
