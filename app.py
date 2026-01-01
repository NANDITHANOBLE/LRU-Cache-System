from flask import Flask, render_template, request, jsonify
from lru_cache import LRUCache

app = Flask(__name__)
cache = LRUCache(3)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/put", methods=["POST"])
def put():
    data = request.json
    cache.put(data["key"], data["value"])
    return jsonify({"message": "Inserted successfully"})

@app.route("/get", methods=["POST"])
def get():
    data = request.json
    value = cache.get(data["key"])
    return jsonify({"value": value})

@app.route("/delete", methods=["POST"])
def delete():
    data = request.json
    result = cache.delete(data["key"])
    return jsonify({"deleted": result})

@app.route("/display")
def display():
    items = []
    curr = cache.head.next
    while curr != cache.tail:
        items.append({"key": curr.key, "value": curr.value})
        curr = curr.next
    return jsonify(items)

if __name__ == "__main__":
    app.run(debug=True)
