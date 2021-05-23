# Aplicatie Bilete

## Utilizare

`docker stack deploy -c portainer-agent-stack.yml`
`docker-compose up`


## Actiuni ce trebuie urmate dupa deploy:

## Adaugarea unui user in mongo:

Se ia id-ul containerului de mongo cu `docker ps`  

Se da comanda `docker exec -it <id container> /bin/bash`  
Se dau comenzile :  
`export MONGODB_DATABASE=flaskdb `   
 `export MONGODB_USERNAME=admin  `  
 `export MONGODB_PASSWORD=admin  `  
 `export MONGODB_HOSTNAME=mongodb`  
 `mongo -u admin -p admin`  
 `use flaskdb`  
 `db.createUser({user: 'admin', pwd: 'admin', roles: [{role: 'readWrite', db: 'flaskdb'}]})`

## Adaugarea Prometheus in Grafana

Se adauga un data source in grafana, selectand prometheus ca sursa  
Se da import la dashbordul cu id-ul 2583 selectand prometheus ca data source
