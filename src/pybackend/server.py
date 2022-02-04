from flask_cors import CORS, cross_origin
from flask import Flask, render_template, request, jsonify

app = Flask(__name__)
CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/config')
@cross_origin()
def get():
    config = request.args.get('type')
    match config:
        case 'vim':
            out = open('out/config.vim', 'r').read()
            return str(out)
        case 'json':
            out = open('out/config.json', 'r').read()
            return str(out)
    
    return 'type argument in not defined'

@app.route('/config/change', methods=['POST'])
@cross_origin()
def change():
    config = request.args.get('type')
    config.headers.add("Access-Control-Allow-Origin", "*")
    match config:
        case 'vim':
            # curl --header "Content-Type: application/json"   --request POST   --data '{"username":"xyz","password":"xyz"}'   http://localhost:5000/config/change?type=vim
            jsonreq = request.get_json(force=True)
            server = jsonreq['settings']['server']
            storage = jsonreq['settings']['storage']
            store = jsonreq['store']
            elems = []

            for i in range(store[len(store)]):
                elems.append(i)
            
            # result = jsonify()
            return f"OK"
        case 'json':
            # return jsonify(request.get_json(force=True))
            return jsonify(request.get_json(force=True))

if __name__ == "__main__":
    app.run(debug=True)