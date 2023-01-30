from flask import Flask, request
import json

app = Flask(__name__)

print("Hey Im here")

@app.route('/orders', methods=['POST'])
def getOrder():
    data = request.json
    print('Order received : ' + json.dumps(data), flush=True)
    return json.dumps({'success': True}), 200, {
        'ContentType': 'application/json'}

app.run(port=8001, host="0.0.0.0")