from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/data', methods=['GET'])
def exchange_crypto():
    lala_sample = {"lala": "ABCDEFGH"}
    return jsonify(lala_sample)


@app.route('/test_api', methods=['GET'])
def test_api():
    data = {"test": "Hello World api testt"}
    return jsonify(data)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8055)