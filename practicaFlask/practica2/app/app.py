#./app/app.py

from bson.json_util import dumps
from pymongo import MongoClient

from flask import Flask, Response, request, jsonify, render_template
from flask_restful import reqparse, abort, Api, Resource

from bson import ObjectId

app = Flask(__name__)
api = Api(app)

# Conectar al servicio (docker) "mongo" en su puerto estandar
client = MongoClient("mongo", 27017)

# Base de datos
db = client.cockteles

class API2(Resource):
    def get(self):
        
        parametro = request.args.get('con')
        if parametro:

            lista = []
            try:
                buscados = db.recipes.find({"ingredients.name":parametro}).sort('name')
            except:
                return "<html><h1>ERROR</h1></html>"
            for recipe in buscados:
                recipe['_id'] = str(recipe['_id']) # casting a string (es un ObjectId)
                lista.append(recipe)
            return jsonify(lista)

        else:

            lista = []
            try:
                buscados = db.recipes.find().sort('name')
            except:
                return "<html><h1>ERROR</h1></html>"
            
            for recipe in buscados:
                recipe['_id'] = str(recipe['_id']) # casting a string (es un ObjectId)
                lista.append(recipe)
            return jsonify(lista)
        
    def post(self):
        receta = request.get_json()
        try:
            db.recipes.insert_one(receta)
        except:
            return "<html><h1>ERROR</h1></html>"
        return dumps(receta)
    
api.add_resource(API2, '/api2/recipes')

class API2_ID(Resource):
    def get(self, id):
        try:
            buscado = db.recipes.find_one({'_id':ObjectId(id)})
        except:
            return "<html><h1>ERROR</h1></html>"
        if buscado:
            buscado['_id'] = str(buscado['_id']) # casting a string (es un ObjectId)
            return jsonify(buscado)
        else:
            return jsonify({'error':'Not found'}), 404

    def delete(self, id):
        try:
            buscado = db.recipes.find_one({'_id':ObjectId(id)})
        except:
            return "<html><h1>ERROR</h1></html>"
        if buscado:
            buscado['_id'] = str(buscado['_id'])
            db.recipes.delete_one({'_id':ObjectId(id)})
            return jsonify(buscado)
        else:
            return jsonify({'error':'Not found'}), 404

    def put(self, id):
        try:
            buscado = db.recipes.find_one({'_id':ObjectId(id)})
        except:
            return "<html><h1>ERROR</h1></html>"
        if buscado:
            receta = request.get_json()
            db.recipes.update_one({'_id':ObjectId(id)},{'$set':receta})
            try:
                buscado = db.recipes.find_one({'_id':ObjectId(id)})
            except:
                return "<html><h1>ERROR</h1></html>"
            buscado['_id'] = str(buscado['_id'])
            return jsonify(buscado)
        else:
            return jsonify({'error':'Not found'}), 404

api.add_resource(API2_ID, '/api2/recipes/<id>')

@app.route('/')
def hola():
    return render_template('index.html')

@app.route('/api/recipes', methods=['GET', 'POST'])
def api_1():
    if request.method == 'GET':
        parametro = request.args.get('con')
        if parametro:

            lista = []
            try:
                buscados = db.recipes.find({"ingredients.name":parametro}).sort('name')
            except:
                return "<html><h1>ERROR</h1></html>"
            for recipe in buscados:
                recipe['_id'] = str(recipe['_id']) # casting a string (es un ObjectId)
                lista.append(recipe)
            return jsonify(lista)

        else:

            lista = []
            try:
                buscados = db.recipes.find().sort('name')
            except:
                return "<html><h1>ERROR</h1></html>"
            
            for recipe in buscados:
                recipe['_id'] = str(recipe['_id']) # casting a string (es un ObjectId)
                lista.append(recipe)
            return jsonify(lista)

    if request.method == 'POST':
        receta = request.get_json()
        try:
            db.recipes.insert_one(receta)
        except:
            return "<html><h1>ERROR</h1></html>"
        
        return dumps(receta)

# para devolver una, modificar o borrar
@app.route('/api/recipes/<id>', methods=['GET', 'PUT', 'DELETE'])
def api_2(id):
    
    try:
        buscado = db.recipes.find_one({'_id':ObjectId(id)})
    except:
        return "<html><h1>ERROR</h1></html>"
    
    if buscado:
        buscado['_id'] = str(buscado['_id'])
        if request.method == 'GET':
            return jsonify(buscado)
        
        if request.method == 'DELETE':
            db.recipes.delete_one({'_id':ObjectId(id)})
            return jsonify(buscado)
        
        if request.method == 'PUT':
            receta = request.get_json()
            db.recipes.update_one({'_id':ObjectId(id)},{'$set':receta})
            buscado = db.recipes.find_one({'_id':ObjectId(id)})
            buscado['_id'] = str(buscado['_id'])
            return jsonify(buscado)
        
    else:
        return jsonify({'error':'Not found'}), 404
    
    """
    if request.method == 'GET':
        buscado = db.recipes.find_one({'_id':ObjectId(id)})
        if buscado:
            buscado['_id'] = str(buscado['_id']) # casting a string (es un ObjectId)
            return jsonify(buscado)
        else:
            return jsonify({'error':'Not found'}), 404

    if request.method == 'PUT':
        buscado = db.recipes.find_one({'_id':ObjectId(id)})
        if buscado:
            buscado['_id'] = str(buscado['_id']) # casting a string (es un ObjectId)
            db.recipes.update_one({'_id':ObjectId(id)})
            return jsonify(buscado)
        else:
            return jsonify({'error':'Not found'}), 404
    
    if request.method == 'DELETE':
        buscado = db.recipes.find_one({'_id':ObjectId(id)})
        if buscado:
            buscado['_id'] = str(buscado['_id']) # casting a string (es un ObjectId)
            db.recipes.delete_one({'_id':ObjectId(id)})
            return jsonify(buscado)
        else:
            return jsonify({'error':'Not found'}), 404
        """

@app.route('/todas_las_recetas')
def mongo():
    # Encontramos los documentos de la coleccion "recipes"
    recetas = db.recipes.find() # devuelve un cursor(*), no una lista ni un iterador

    lista_recetas = []
    for  receta in recetas:
        app.logger.debug(receta)  # salida consola
        lista_recetas.append(receta)

    response = {
        'len': len(lista_recetas),
        'data': lista_recetas
    }

    # Convertimos los resultados a formato JSON
    resJson = dumps(response)

    # Devolver en JSON al cliente cambiando la cabecera http para especificar que es un json
    return Response(resJson, mimetype='application/json')

@app.route('/recetas_de/<cadena>')
def recetas_de(cadena):
    recetas = db.recipes.find({"slug":cadena})

    lista_recetas = []
    for  receta in recetas:
        app.logger.debug(receta)  # salida consola
        lista_recetas.append(receta)

    response = {
        'len': len(lista_recetas),
        'data': lista_recetas
    }

    # Convertimos los resultados a formato JSON
    resJson = dumps(response)

    # Devolver en JSON al cliente cambiando la cabecera http para especificar que es un json
    return Response(resJson, mimetype='application/json')
    

@app.route('/recetas_con/<cadena>')
def recetas_con(cadena):
    recetas = db.recipes.find({"ingredients.name":cadena})
    
    lista_recetas = []
    for  receta in recetas:
        app.logger.debug(receta)  # salida consola
        lista_recetas.append(receta)

    response = {
        'len': len(lista_recetas),
        'data': lista_recetas
    }

    # Convertimos los resultados a formato JSON
    resJson = dumps(response)

    # Devolver en JSON al cliente cambiando la cabecera http para especificar que es un json
    return Response(resJson, mimetype='application/json')

@app.route('/recetas_compuestas_de/<int:numero>/<cadena>')
def recetas_compuestas_de(numero, cadena):
    recetas = db.recipes.find({cadena:{"$size":numero}})
    
    lista_recetas = []
    for  receta in recetas:
        app.logger.debug(receta)  # salida consola
        lista_recetas.append(receta)

    response = {
        'len': len(lista_recetas),
        'data': lista_recetas
    }

    # Convertimos los resultados a formato JSON
    resJson = dumps(response)

    # Devolver en JSON al cliente cambiando la cabecera http para especificar que es un json
    return Response(resJson, mimetype='application/json')