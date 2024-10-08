from flask import Flask, request, jsonify, render_template
from flask_cors import CORS
import hashlib

f = Flask(__name__)
CORS(f)

@f.route('/')
def index():
    return render_template('index.html')

@f.route('/hash', methods=['GET'])
def hash_number():
    number = request.args.get('number', '')
    if number:
        hashed_number = hashlib.sha256(number.encode()).hexdigest()
        return jsonify({'number': number, 'hashed': hashed_number})
    return jsonify({'error': 'No number provided'}), 400

if __name__ == '__main__':
    f.run(debug=True)

