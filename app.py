from flask import Flask
from flask_restful import Api, Resource

app = Flask(__name__)
api = Api(app)

@app.after_request
def add_cors_headers(response):
    response.headers['Access-Control-Allow-Origin'] = 'http://localhost:3000'
    response.headers['Access-Control-Allow-Headers'] = 'Content-Type'
    response.headers['Access-Control-Allow-Methods'] = 'GET'
    return response

class DataResource(Resource):
    def get(self):
        data = {"message": "hellow"}
        return data

api.add_resource(DataResource, '/api/data')

if __name__ == '__main__':
    app.run()
