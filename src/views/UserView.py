from flask import request, json, Response, Blueprint, jsonify
from ..models.UserModel import User, UserSchema

user_api = Blueprint('users', __name__)
user_serializer = UserSchema()


@user_api.route("/")
def get_users():
    # query data
    users = User.query.all()

    # Serialize the data for the response
    data = user_serializer.dump(users, many=True)
    return jsonify(data), 200


@user_api.route("/", methods=['POST'])
def create_users():
    request_data = request.get_json()
    data = user_serializer.load(request_data)

    user = User(data)
    user.save()
    return jsonify(user_serializer.dump(user)), 201


@user_api.route("/<user_id>")
def get_user_detail(user_id):
    user = User.query.get(user_id)
    return jsonify(user_serializer.dump(user)), 200


@user_api.route("/<user_id>", methods=['DELETE'])
def delete_user(user_id):
    user = User.query.get(user_id).delete()
    return "delete success"
