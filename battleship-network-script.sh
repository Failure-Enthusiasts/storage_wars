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
# docker build -t battleship-image . --no-cache 
docker build -t battleship-image -f Dockerfile-API . --no-cache 

# create the network for the containers to talk 
docker network create --driver bridge storagewars-net

# start both containers
docker run -dit --name container1 --network storagewars-net battleship-image
docker run -dit --name container2 --network storagewars-net battleship-image

# check that everything is up
docker container ls
docker network ls

#curl --location --request POST 'container2:5000/fire' --header 'Content-Type: application/json' --data-raw '{ "x": 1, "y": 2}'