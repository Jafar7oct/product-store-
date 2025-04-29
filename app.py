from flask import Flask, render_template, request, jsonify
import uuid

app = Flask(__name__)

# Sample product data with local images
products = [
    {"id": str(uuid.uuid4()), "name": "Wireless Headphones", "price": 89.99, "description": "High-quality noise-cancelling headphones", "image": "/static/1.jpg"},
    {"id": str(uuid.uuid4()), "name": "Smartwatch", "price": 199.99, "description": "Fitness tracker with heart rate monitor", "image": "/static/2.jpg"},
    {"id": str(uuid.uuid4()), "name": "Laptop Stand", "price": 29.99, "description": "Ergonomic aluminum stand", "image": "/static/3.jpg"},
    {"id": str(uuid.uuid4()), "name": "USB-C Hub", "price": 49.99, "description": "Multi-port adapter for laptops", "image": "/static/4.jpg"},
]

@app.route('/')
def index():
    return render_template('index.html', products=products)

@app.route('/search', methods=['GET'])
def search():
    query = request.args.get('q', '').lower()
    filtered_products = [p for p in products if query in p['name'].lower() or query in p['description'].lower()]
    return jsonify(filtered_products)

if __name__ == '__main__':
    app.run(debug=True)