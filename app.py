from urllib.parse import parse_qs

from flask import Flask, request
from flask_restful import Api, Resource
from models.user import add_user, check_user
import hashlib

app = Flask(__name__)
api = Api(app)

@app.after_request
def add_cors_headers(response):
    response.headers['Access-Control-Allow-Origin'] = 'http://localhost:3000'
    response.headers['Access-Control-Allow-Headers'] = 'Content-Type'
    response.headers['Access-Control-Allow-Methods'] = 'GET, POST'
    return response

class DataResource(Resource):
    def get(self):
        data = {"message":"Hello, GET request!"}
        return data

    def post(self):
        # email = request.form.get('email')
        # password = request.form.get('password')
        data = request.get_json()

        email = data['email']
        password = data['password']

        print("Email:", email)
        print("Password:", password)

        hash_password = hashlib.sha256(password.encode()).hexdigest()
        if check_user(email):
            add_user(email, hash_password)
            return {"message": "user added successfully"}
        else:
            return {"message": "there is already a user with this email"}


api.add_resource(DataResource, '/api/data')

if __name__ == '__main__':
    app.run()
