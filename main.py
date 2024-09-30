from flask import Flask
from flask_restx import Api, Resource


app = Flask(__name__)

api = Api(app,doc='/docs')

@api.route('/hello')
class HelloResource(Resource):
    def get(self):
        return {"message": "Hello World"}
    


if __name__ == '__main__':
    app.run()

