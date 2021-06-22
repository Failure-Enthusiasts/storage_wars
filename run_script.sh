sh cleanup.sh
sh battleship-network-script.sh
# docker ps --format "{{.Names}}"

# docker exec -it container1  bash
# docker run -it -p 80:80 container1 bash 
docker run -d -p 6000:5000 battleship-image

# then run this, does successfully hit the container from localhost:

# curl --location --request POST '127.0.0.1:6000/fire' --header 'Content-Type: application/json' --data-raw '{
#     "x": 0,
#     "y": 0
# }'

# curl --location --request POST '127.0.0.1:6000/cheat'     

