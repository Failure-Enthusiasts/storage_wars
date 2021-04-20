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

docker build -t pizzaparty .

docker network create --driver bridge storagewars-net

docker run -dit --name container1 --network storagewars-net pizzaparty
docker run -dit --name container2 --network storagewars-net pizzaparty


# check that everything is up
docker container ls
docker network ls

# docker container attach alpine1
# ping -c 2 alpine2

echo $'PING TIME \n\n'

# docker exec -d alpine1 ping -c 2 google.com
docker exec -it container1 echo "HELLO FROM THE OTHER SIDE"
docker exec -it container1 ping -c 2 container2

echo $'END PING TIME \n\n'
read -p "Press any key to quit."
# cleanup 
docker container stop container1 container2
docker container rm container1 container2
docker network rm storagewars-net
docker container ls
docker network ls