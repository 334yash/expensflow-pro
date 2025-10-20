from flask import Flask, jsonify, request
app = Flask(__name__)
expenses = []

@app.route("/health")
def health():
    return "ok"

@app.route("/expenses", methods=["GET","POST"])
def expenses_route():
    if request.method == "POST":
        data = request.json
        expenses.append(data)
        return jsonify({"status":"created"}), 201
    return jsonify(expenses)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
