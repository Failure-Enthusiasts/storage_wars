# based off: https://docs.docker.com/network/network-tutorial-standalone/ 

# check if docker is up or not
result=$( docker ps )

if [[ -n "$result" ]];
then
  echo $result
  echo "Docker is up"
else
  echo $result
  echo "Docker isn't up yet"
  open -a Docker
  sleep 45 # wait 45s (maybe we can shorten it)
fi

# build the docker image
docker build -t battleship-image .

# create the network for the containers to talk 
docker network create --driver bridge storagewars-net

# start both containers
docker run -dit --name container1 --network storagewars-net battleship-image
docker run -dit --name container2 --network storagewars-net battleship-image


# check that everything is up
docker container ls
docker network ls

# hop into container2
docker exec -it container2 echo "HELLO FROM THE OTHER SIDE"


# cleanup the containers, and images
echo $'CLEANUP \n\n'
read -p "Press any key to quit."

docker container stop container1 container2
docker container rm container1 container2
docker network rm storagewars-net
docker container ls
docker network ls