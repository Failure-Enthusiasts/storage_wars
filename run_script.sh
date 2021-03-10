docker network create --driver bridge alpine-net

docker run -dit --name alpine1 --network alpine-net alpine ash
docker run -dit --name alpine2 --network alpine-net alpine ash
docker run -dit --name alpine3 alpine ash

docker container ls
docker network ls
# echo 'before stop'
# docker stop $(docker ps -a -q)
# docker rm $(docker ps -a -q)

docker container attach alpine1
ping -c 2 alpine2


# cleanup 
docker container stop alpine1 alpine2 alpine3
docker container rm alpine1 alpine2 alpine3
docker network rm alpine-net
docker container ls
docker network ls