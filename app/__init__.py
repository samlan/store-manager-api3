from flask import Flask 
from flask_restful import Api
from instance.config import app_config
from .api.v1.views import Products,ProductsList,myblueprint


#register blueprint

api = Api(myblueprint)

def create_app(config_name):
    app = Flask(__name__,instance_relative_config=True)
    app.register_blueprint(myblueprint)
    app.config.from_pyfile('config.py')
    #map blueprint to API endpoint
    api.add_resource(ProductsList,'/products')
    api.add_resource(Products,'/products/<product_id>')
    return app
