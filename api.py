from flask import Flask, request, jsonify

apl = Flask(__name__)

@apl.route("/get-user/<user_id>")
def get_user(user_id):
    user_data = {
        "user_id" : user_id,
        "nama" : "Bal bal",
        "email" : "lalalal@gmail.com" 
    }

    extra = request.args.get("extra")
    if extra:
        user_data["extra"] = extra

    return jsonify(user_data), 200

@apl.root("/create-user", methods =["POST"])
def create_user():
    data = request.get_json()
    return jsonify(data), 201

if __name__ == "__main__":
    apl.run(debug=True)