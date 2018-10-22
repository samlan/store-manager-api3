from flask import Flask, request,Blueprint,jsonify
from flask_restful import Resource, Api, abort,reqparse


#test data dictionaries
sales ={ 
    2:{'id':'2','prodname':'Iphone X','category':'mobile phones','price':'$1550','img':''},
    9:{'id':'9', 'prodname':'Google Pixel','category':'mobile phones','price':'$800','img':''},
    8:{'id':'8', 'prodname':'Macbook Pro','category':'laptop','price':'$1800','img':''},
    7:{'id':'7','prodname':'Lenovo Yoga','category':'laptop','price':'$690','img':''},
    3:{'id':'3','prodname':'LG TV','category':'flatscreen','price':'$550','img':''},
    1:{'id':'1', 'prodname':'Samsung TV','category':'flatscreen','price':'$450','img':''}
	}

products = {
     2:{'id':'2','prodname':'Iphone X','category':'mobile phones','price':'$1550','img':''},
    9:{'id':'9', 'prodname':'Google Pixel','category':'mobile phones','price':'$800','img':''},
    8:{'id':'8', 'prodname':'Macbook Pro','category':'laptop','price':'$1800','img':''},
    7:{'id':'7','prodname':'Lenovo Yoga','category':'laptop','price':'$690','img':''},
    3:{'id':'3','prodname':'LG TV','category':'flatscreen','price':'$550','img':''},
    1:{'id':'1', 'prodname':'Samsung TV','category':'flatscreen','price':'$450','img':''},
    12:{'id':'12','prodname':'Toshiba TV','category':'flatscreen','price':'$655','img':''},
    4:{'id':'4', 'prodname':'Sony TV','category':'flatscreen','price':'$800','img':''},
    5:{'id':'5', 'prodname':'Samsung S8','category':'mobile phone','price':'$1100','img':''},
    71:{'id':'71','prodname':'Iphone 7','category':'mobile phone','price':'$390','img':''},
    33:{'id':'33','prodname':'LG TV','category':'flatscreen','price':'$550','img':''},
    11:{'id':'11', 'prodname':'Samsung TV','category':'flatscreen','price':'$450','img':''}
		
}

myblueprint = Blueprint('api', __name__, url_prefix='/api/v1')

parser = reqparse.RequestParser()
parser.add_argument('product')

# shows a single product item and lets you delete a product item


class ProductsList(Resource):
    def get(self):
        return products

class Products(Resource):
    
    def get(self,product_id):
        if int(product_id) not in products.keys():
            abort(404, message="Product {} doesn't exist".format(product_id))
        return jsonify(products[int(product_id)])
    
    def delete(self, product_id):
        if int(product_id) not in products.keys():
             abort(404, message="Product {} doesn't exist".format(product_id))
        del products[int(product_id)]
        return products
    
    def put(self, product_id):
        if int(product_id) not in products.keys():
            abort(404,message = "Product {} doesn't exist".format(product_id))
        args = parser.parse_args()
        #new_prod = {'task': args['task']}
        products[int(product_id)] = args
        return  products   


