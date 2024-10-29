from flask import Flask, jsonify
import models
import jwt
import datetime

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret_key_here'  

def generate_token(username: str):
    expiration_time = datetime.datetime.utcnow() + datetime.timedelta(minutes=30)  
    token = jwt.encode({'username': username, 'exp': expiration_time}, app.config['SECRET_KEY'], algorithm='HS256')
    return token

@app.route('/authenticate/<username>', methods=['GET'])
def authenticate(username):
    userdata = models.User.get_or_none(models.User.username == username)
    if userdata is None:
        return jsonify({'status': 'ERROR', 'message': 'USER DOES NOT EXIST'}), 401

    token = generate_token(username)
    
    return jsonify({'username': username, 'status': 'success', 'token': token})

if __name__ == '__main__':
    app.run(debug=True)

