from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/endpoint1', methods=['POST'])
def endpoint1():
    data = request.json
    parameter = data.get('parameter', None)
    return jsonify({'result': 'Endpoint 1', 'parameter': parameter})

@app.route('/endpoint2', methods=['POST'])
def endpoint2():
    data = request.json
    parameter = data.get('parameter', None)
    return jsonify({'result': 'Endpoint 2', 'parameter': parameter})

@app.route('/endpoint3', methods=['POST'])
def endpoint3():
    data = request.json
    parameter = data.get('parameter', None)
    return jsonify({'result': 'Endpoint 3', 'parameter': parameter})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=False)
