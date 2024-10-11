from flask import Flask, jsonify

app = Flask(__name__)

# Dummy data for the user information
users = [
    {
        "id": 1,
        "username": "user1",
        "email": "user1@example.com",
        "full_name": "John Doe",
        "age": 30,
        "country": "United States"
    },
    {
        "id": 2,
        "username": "user2",
        "email": "user2@example.com",
        "full_name": "Jane Smith",
        "age": 28,
        "country": "Canada"
    },
    {
        "id": 3,
        "username": "user3",
        "email": "user3@example.com",
        "full_name": "Mike Johnson",
        "age": 35,
        "country": "Australia"
    }
]

@app.route('/api/users', methods=['GET'])
def get_users():
    return jsonify(users)

@app.route('/api/users/<int:user_id>', methods=['GET'])
def get_user(user_id):
    user = next((user for user in users if user["id"] == user_id), None)
    if user:
        return jsonify(user)
    return jsonify({"message": "User not found"}), 404

# Optional: Handle the root path
@app.route('/', methods=['GET'])
def home():
    return jsonify({"message": "Welcome to the User Information API"}), 200

# Optional: Handle favicon requests
@app.route('/favicon.ico')
def favicon():
    return '', 204

if __name__ == '__main__':
    app.run(debug=True)
