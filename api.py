from flask import Flask, request, jsonify

app = Flask(__name__)

# Load HWID keys from a file
def load_keys():
    with open('HWID_keys_with_postfix.txt', 'r') as file:
        keys = [line.strip() for line in file.readlines()]
    return keys

@app.route('/validate_hwid', methods=['POST'])
def validate_hwid():
    hwid_key = request.json.get('hwid')
    keys = load_keys()

    if hwid_key in keys:
        return jsonify({'status': 'valid'}), 200
    else:
        return jsonify({'status': 'invalid'}), 400

if __name__ == '__main__':
    app.run(debug=True)
