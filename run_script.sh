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

docker network create --driver bridge alpine-net

docker run -p 5000:5000 -dit --name alpine1 --network alpine-net alpine ash
docker run -p 5001:5001 -dit --name alpine2 --network alpine-net alpine ash
docker run -p 5002:5002 -dit --name alpine3 alpine ash

# check that everything is up
docker container ls
docker network ls

# docker container attach alpine1
# ping -c 2 alpine2

echo $'PING TIME \n\n'

# docker exec -d alpine1 ping -c 2 google.com
docker exec -it alpine1 echo "HELLO FROM THE OTHER SIDE"
docker exec -it alpine1 ping -c 2 alpine2

echo $'END PING TIME \n\n'
read -p "Press any key to quit."
# cleanup 
docker container stop alpine1 alpine2 alpine3
docker container rm alpine1 alpine2 alpine3
docker network rm alpine-net
docker container ls
docker network ls