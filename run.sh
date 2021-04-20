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

docker network create --driver bridge container-network

docker build -t pizzaparty .
docker run -d --name container1 --expose 5000 --network container-network pizzaparty
docker run -d --name container2 --expose 5000 --network container-network pizzaparty

# docker stop $(docker ps -a -q)
# docker rm $(docker ps -a -q)
# docker network rm container-network
