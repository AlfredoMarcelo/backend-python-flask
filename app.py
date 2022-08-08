from flask import Flask, jsonify, render_template, request


app = Flask(__name__)

datos = [{'name': 'Renata', 'color': 'black'}]

@app.route("/", methods=['GET'])
def holaMundo():
    return render_template('index.html');

@app.route("/todos", methods=['GET'])
def todos():
    if request.method == 'GET':
        return jsonify(datos), 200
        
if __name__ == '__main__':
    app.run(debug=True)