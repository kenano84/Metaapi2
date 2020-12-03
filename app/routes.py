from app import app
from flask import Response, request
import json
import controllers.users_controller as usc

@app.route("/")
def index():
    return "Welcome"

@app.route('/users', methods=['GET'])
def get_all_users():
    users = usc.get_all_users()
    return Response(json.dumps(users), mimetype='application/json')

@app.route('/users', methods=['POST'])
def add_user():
    data = request.get_json()
    usc.add_user(data)
    return json.dumps({'Success': True}), 201, {'ContentType': 'application/json'}


@app.route('/users/<string:id>', methods=['GET', 'DELETE', 'PUT'])
def get_user_by_id(id):
    user = usc.get_user_by_id(id)
    return Response(json.dumps(user), mimetype='application/json')

def delete_user_by_id(id):

    # vi använder inte någon lista som heter "users" eftersom vi har strukturerat vårat projekt enlgt mvc(model-view-controller) (mappstrukturen)
        i = 0;
        for user in get_user_by_id:
            if get_user_by_id["id"] == id:
                users.pop( i )
                response = Response( "", status=204 )
                return response
            i += 1

        response = Response("", status=404, mimetype='application/json')
        return response

def put_user_by_id(id):
    request_data = request.get_json()
    usc.change_entire_user_info(id, request_data)
    response = Response(json.dumps({"status": "Complete user update performed"}, status=204))
    return response


    # vad har koden nedan för syfte? att stoppa in den på rätt id-rad? tänker att vi inte behöver
    # det iom att vi skickar in till databasen samma primary key... men kanske tänker fel
    i = 0;
    for user in users:
        current_id = user["id"]
    if current_id == id():
            user[i] = new_user_id
            i += 1
    response = Response("", status=204)
    return response

@app.route('/users/<string:id>', methods=['PATCH'])
def patch_user(id):
    request_data = request.get_json()
    usc.change_fields(id, request_data)
    pass


