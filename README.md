# storage_wars

## This repo currently spins up a docker container that sleeps for 3000000 seconds. 

The flow works like this:

- You write a Dockerfile (the plans for the blueprint for our Container). 
- You `docker build` it into an Image (our blueprint). 
- Then, you launch the Container via `docker run`.

The commands are:

1. `docker build .`
2. `docker run -d <image-id>`

To see if this worked,
3. `docker ps`, look for running containers.
4. `docker exec -it <container ID> bash`

When done, 
5. `docker stop <container-id>`
6. `docker rm <container-id>`
