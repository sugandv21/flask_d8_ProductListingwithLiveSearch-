from flask import Flask, render_template, jsonify, request

app = Flask(__name__, template_folder="../frontend")

products = [
    {"id": 1, "name": "Laptop", "price": 65000, "description": "Powerful laptop with 16GB RAM"},
    {"id": 2, "name": "Smartphone", "price": 25000, "description": "Latest Android phone"},
    {"id": 3, "name": "Headphones", "price": 2000, "description": "Noise cancelling headphones"},
    {"id": 4, "name": "Keyboard", "price": 1200, "description": "Mechanical keyboard"},
    {"id": 5, "name": "Monitor", "price": 15000, "description": "27-inch Full HD display"},
]

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/api/products")
def get_products():
    query = request.args.get("q", "").lower()
    filtered = [p for p in products if query in p["name"].lower() or query in p["description"].lower()]
    return jsonify(filtered)

if __name__ == "__main__":
    app.run(debug=True)
