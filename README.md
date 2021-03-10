# storage_wars

## This repo currently spins up a docker container that sleeps for 3000000 seconds. 

1. `docker build .`
2. `docker run -d <image-id>`
3. `docker ps`
4. `docker stop <container-id>`
5. `docker rm <container-id>`

You can also stop and remove all. 
4. `docker stop $(docker ps -a -q)`
5. `docker rm $(docker ps -a -q)`