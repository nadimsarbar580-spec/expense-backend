from flask import Flask, jsonify, request
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# In-memory database
expenses = [
    {"id": 1, "title": "Lunch", "amount": 150, "category": "Food"},
    {"id": 2, "title": "Bus fare", "amount": 30, "category": "Transport"},
]
next_id = 3

# GET — return all expenses
@app.route('/expenses', methods=['GET'])
def get_expenses():
    return jsonify(expenses), 200

# POST — add a new expense
@app.route('/expenses', methods=['POST'])
def add_expense():
    global next_id
    data = request.get_json()

    if not data:
        return jsonify({"error": "No data provided"}), 400
    if not data.get("title") or not isinstance(data["title"], str):
        return jsonify({"error": "'title' is required and must be text"}), 400
    if data.get("amount") is None or not isinstance(data["amount"], (int, float)) or data["amount"] <= 0:
        return jsonify({"error": "'amount' must be a positive number"}), 400
    if not data.get("category") or not isinstance(data["category"], str):
        return jsonify({"error": "'category' is required"}), 400

    expense = {
        "id": next_id,
        "title": data["title"],
        "amount": data["amount"],
        "category": data["category"]
    }
    expenses.append(expense)
    next_id += 1
    return jsonify(expense), 201

if __name__ == '__main__':
    app.run(debug=True)