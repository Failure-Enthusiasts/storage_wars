sh cleanup.sh
sh battleship-network-script.sh
# docker ps --format "{{.Names}}"

docker exec -it container1 bash
flask api.py