from flask import Blueprint, request, jsonify 
from flask_jwt_extended import create_access_token, jwt_required 
from rangers_shop.models import Customer, Product, ProdOrder, Order, db, product_schema, products_schema 



api = Blueprint('api', __name__, url_prefix='/api')


@api.route('/token', methods = ['GET', 'POST'])
def token():

    data = request.json()
    if data:
        client_id = data['client_id']
        access_token = create_access_token(identity=client_id) #just needs a unique identifier 
        return {
            'status': 200,
            'access_token': access_token
        }
    else:
        return {
            'status' : 400,
            'message' : 'Missing Client Id. Try Again.'
        } 
        