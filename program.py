from flask import Flask, request, jsonify
from waitress import serve
import json

app = Flask(__name__)

offers = []

@app.route('/addOffer', methods=['POST'])
def addOffer():
    data = request.json
    offer = data.get('offer', None)
    offers.append({len(offers) : offer})
    return jsonify({'Offer added': offer})

@app.route('/getOffers', methods=['GET'])
def getOffers():
    return jsonify(offers)

@app.route('/flushOffers', methods=['POST'])
def flushOffers():
    offers.clear()
    return []

if __name__ == '__main__':
    # Debug/Development
    # .run(debug=True)
    # Production
    serve(app, host="0.0.0.0", port=9999)
