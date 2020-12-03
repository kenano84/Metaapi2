import model.repository.users_repo as gr
from flask import request


def get_all_users():
    users = gr.UsersRepo.get_all_users()
    users = [user.to_dict() for user in users]
    return users

def get_user_by_id(id):
    gr.UsersRepo.get_user_by_id(id)
    return user

def add_user():
    gr.UsersRepo.create_user(data)
    return

def change_entire_user_info(id, new_user_data):
    new_user = new_user_data(id, request_data['username'], request_data['password'], request_data['email'], request_data['apis'])
    gr.UsersRepo.changed_user(id, new_user)
    return

def change_fields(id, request_data):
    if "username" in request_data:
        username = request_data['username']
        gr.UsersRepo.change_username (id, "username")
        return

    if "password" in request_data:
        password = request_data['password']
        gr.UsersRepo.change_password(id, password)
        return

    if "email" in request_data:
        email = request_data['email']
        gr.UsersRepo.change_email(id, email)
        return

    if "apis" in request_data:
        apis = request_data['apis']
        gr.UsersRepo.change_apis(id, email)
        return
    return