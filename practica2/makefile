all: post  put delete

up:
	docker-compose up -d

down:
	docker-compose down

get:
	http GET http://localhost:5000/api/recipes
	
get_con:
	http GET http://localhost:5000/api/recipes?con=Vodka
	
get_id:
	http GET http://localhost:5000/api/recipes/634841701afb7c6a87b633ed

post:
	http POST http://localhost:5000/api/recipes name="Bebida prueba" slug="bebida-prueba" instructions:='["Instrucciones de prueba"]' ingredients:='[{"name": "Scotch", "quantity": { "quantity":"1", "unit":"oz"}}]' 

put:
	http PUT http://localhost:5000/api/recipes/634841701afb7c6a87b633ed instructions:='["Instrucciones nuevas"]'

delete:
	http DELETE http://localhost:5000/api/recipes/634843be1afb7c6a87b633ee

restaurar_bd:
	docker-compose exec mongo /bin/bash
	mongoimport --db cockteles --collection recipes dump/cockteles/recipes.json