
from flask import Flask, jsonify, render_template, request



app = Flask(__name__)

datos = [{'name': 'Renata', 'color': 'black'}]

@app.route("/", methods=['GET'])
def holaMundo():
    return render_template('index.html');

@app.route("/todos", methods=['GET', 'POST'])
def todos():
    if request.method == 'GET':
        return jsonify(datos), 200
    if request.method == 'POST':
        data = request.get_json()
        if data['nombre'] == '':
            return jsonify({"msg":"El nombre es requerido."}),400
        return jsonify(data)
    return jsonify({"msg": "todo ok"}), 201

@app.route("/todos/<int:id>", methods=['PUT'])
def put_todos(id = None):
    if request.method == 'PUT':
        if id is not None:
            nombre = request.json.get("nombre", "vacio")
            return jsonify({"msg": "todo ok", "nombre":nombre}), 200
        else:
            return jsonify({"msg": "id es requerido"}), 400
        
if __name__ == '__main__':
    app.run(debug=True)