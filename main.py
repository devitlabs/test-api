from flask import Flask
from flask_restful import Resource, Api
from datetime import datetime

app = Flask(__name__)
api = Api(app)

class HelloWorld(Resource):
    def get(self):
        date = datetime.now()
        return {'date': f"{date}"}

api.add_resource(HelloWorld, '/')

if __name__ == '__main__':
    app.run(debug=False,port=4535,host="0.0.0.0")