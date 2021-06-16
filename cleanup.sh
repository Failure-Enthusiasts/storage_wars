# script to rm the containers and reset the environment
docker container stop container1 container2
docker container rm container1 container2
docker network rm storagewars-net
docker container ls
docker network ls