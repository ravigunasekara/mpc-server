from flask import Flask, request, jsonify

app = Flask(__name__)

users = [
    {"cafe_id": "1A88EBA6-5798-452D-AEA6-21103DF73A38", "email": "alice@example.com"},
    {"cafe_id": "7A70AFDE-10F3-4872-8249-205BD4F01201", "email": "bob@example.com"},
    {"cafe_id": "C81C4D4E-19FE-47EF-BDE4-7460A70AF23C", "email": "charlie@example.com"}
]


@app.route('/user', methods=['GET'])
def get_user_id():
    email = request.args.get('email')
    if not email:
        return jsonify({"error": "Email query parameter is required"}), 400

    user = next((u for u in users if u['email'].lower() == email.lower()), None)
    if user:
        return jsonify({"id": user['cafe_id']})
    else:
        return jsonify({"error": "User not found"}), 404

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=7070)