# storage_wars
## This repo currently spins up a docker container that sleeps for 3000000 seconds. 

## Note: Still in progress. 

The flow works like this:

- You write a Dockerfile (the plans for the blueprint for our Container). 
- You `docker build` it into an Image (our blueprint). 
- Then, you launch the Container via `docker run`.

The commands are:

1. `docker build .`
2. `docker run -d <image-id>`
3. `docker ps`

To see if this worked,

3. `docker ps`, look for running containers.
4. `docker exec -it <container ID> bash`

When done, you can stop and remove.

5. `docker stop <container-id>` or `docker stop $(docker ps -a -q)`
6. `docker rm <container-id>` or `docker rm $(docker ps -a -q)`

For run_script.sh,

* Use `chmod 777 run_script.sh`

# Bonus - Going Into One Container and Reaching Out to Another One 
* exposes the port for the container with `docker build --tag python-docker .`
* `docker run -d -p 5000:5000 <image>`
* https://docs.docker.com/config/containers/container-networking/
* go into the container with `docker exec -it <container-id> bash`
* install curl `apt-get update` and `apt-get install curl` inside the container
* `curl --location --request GET '0.0.0.0:5000'`