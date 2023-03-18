API=http://localhost:5000/api/recipes
API2=http://localhost:5000/api2/recipes


all: up get_con get_id put get_id post delete down

up:
	docker-compose up -d

down:
	docker-compose down

get_all: get get_con get_id

get:
	http GET $(API)
	
get_con:
	http GET $(API)?con=Vodka
	
get_id:
	http GET $(API)/634951f411e690f9b54a3ee6

get_all2: get2 get_con2 get_id2

get2:
	http GET $(API2)
	
get_con2:
	http GET $(API2)?con=Vodka
	
get_id2:
	http GET $(API2)/634951f411e690f9b54a3ee6

post:
	http POST $(API) name="Bebida prueba" slug="bebida-prueba" instructions:='["Instrucciones de prueba22"]' ingredients:='[{"name": "Scotch", "quantity": { "quantity":"1", "unit":"oz"}}]' 

post2:
	http POST $(API2) name="Bebida prueba" slug="bebida-prueba" instructions:='["Instrucciones de prueba22"]' ingredients:='[{"name": "Scotch", "quantity": { "quantity":"1", "unit":"oz"}}]' 

put:
	http PUT $(API)/634951f411e690f9b54a3ee6 instructions:='["Instrucciones nuevas"]'

put2:
	http PUT $(API2)/634951f411e690f9b54a3ee6 instructions:='["Instrucciones nuevas api2"]'

delete:
	http DELETE $(API)/634951f411e690f9b54a3ee6

delete2:
	http DELETE $(API2)/634951f411e690f9b54a3ee6

restaurar_bd:
	mkdir datos_db
	docker-compose exec mongo /bin/bash
	mongoimport --db cockteles --collection recipes dump/cockteles/recipes.json