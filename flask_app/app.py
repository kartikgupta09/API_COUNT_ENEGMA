# flask_app/app.py

from flask import request, jsonify
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy

from . import create_app, db
from .models import APIHit
from datetime import datetime

app = create_app()

# db = SQLAlchemy()
# db.init_app(app)
CORS(app)


def create_tables():
    db.create_all()

@app.route('/api/track', methods=['POST'])
def track_api():
    data = request.get_json()
    new_hit = APIHit(
        request_id=data['RequestId'],
        request_type=data['RequestType'],
        request_time=datetime.strptime(data['RequestTime'], '%Y/%m/%d %H:%M'),
        payload=data.get('Payload'),
        content_type=data.get('Content-type'),
        ip_address=data['IP address'],
        os=data['OS'],
        user_agent=data['UserAgent']
    )
    db.session.add(new_hit)
    db.session.commit()
    return jsonify({"message": "API hit recorded"}), 201


@app.route('/api/hits', methods=['GET'])
def get_hits():
    hits = APIHit.query.all()
    return jsonify([{
        'id': hit.id,
        'request_id': hit.request_id,
        'request_type': hit.request_type,
        'request_time': hit.request_time,
        'payload': hit.payload,
        'content_type': hit.content_type,
        'ip_address': hit.ip_address,
        'os': hit.os,
        'user_agent': hit.user_agent
    } for hit in hits])


if __name__ == '__main__':
    app.run(debug=True)
