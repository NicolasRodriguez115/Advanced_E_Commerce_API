from flask import request, jsonify
from models.schemas.orderSchema import order_schema, orders_schema
from services import orderService
from marshmallow import ValidationError
from caching import cache
from utils.util import token_required, admin_required

@token_required
def create_order():
    try:
        order_data = order_schema.load(request.json)
    except ValidationError as e:
        return jsonify(e.messages), 400
    
    new_order = orderService.create_order(order_data)
    return order_schema.jsonify(new_order), 201

@token_required
@cache.cached(timeout=60)
def get_by_id(order_id):
    response, status = orderService.get_by_id(order_id)
    if status == 404:
        return jsonify(response), status
    return order_schema.jsonify(response), status