from flask import Flask, request, jsonify

app = Flask(__name__)

users = [
    {"id": 1, "email": "alice@example.com"},
    {"id": 2, "email": "bob@example.com"},
    {"id": 3, "email": "charlie@example.com"}
]

@app.route('/hello', methods=['GET'])
def hello():
    return jsonify({"message": "Hello from Flask!"})

@app.route('/user', methods=['GET'])
def get_user_id():
    email = request.args.get('email')
    if not email:
        return jsonify({"error": "Email query parameter is required"}), 400

    user = next((u for u in users if u['email'].lower() == email.lower()), None)
    if user:
        return jsonify({"id": user['id']})
    else:
        return jsonify({"error": "User not found"}), 404

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)