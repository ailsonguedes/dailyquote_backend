from flask import Blueprint, jsonify
from api.models.quotes import Quote

bp = Blueprint('api', __name__)

@bp.route('/api/quotes', methods=['GET'])
def get_quotes():
    quotes = Quote.query.all()
    return jsonify([quote.to_dict() for quote in quotes])

@bp.route('/api/quote/<int:id>', methods=['GET'])
def get_quote_by_id(id):
    quote = Quote.query.get(id)
    if quote:
        return jsonify(quote.to_dict())
    else:
        return jsonify({"error":"Quote not found"}), 404  
