__author__ = 'tekvy'
from flask import render_template, request, Response, redirect, url_for
import json
from app import app
import os
import gcm_test
import repository


@app.route("/")
def hello():
    return render_template('index.html')

@app.route("/register", methods=['POST'])
def register_user():
    # add user to db
    user_name = request.form.get('user_name')
    user_email = request.form.get('user_email')
    user_password = request.form.get('user_password')
    gcm_regid = request.form.get('gcm_regid')

    repository.add_user(user_name, user_email, user_password, gcm_regid)
    js = [{"name": user_name, "user_email": user_email,  "gcm_regid": gcm_regid}]
    return Response(json.dumps(js),  mimetype='application/json')


@app.route("/getusers", methods=['GET'])
def get_user():
    a = repository.get_users()
    return Response(json.dumps(a),  mimetype='application/json')


@app.route("/sendgcm", methods=['POST'])
def send_gcm():

    user_email = request.form.get('user_email')
    header = request.form.get('header')
    content = request.form.get('content')
    a = repository.return_user_details(user_email)
    regid = a["gcm_regid"]
    # call gcm method and pass gcm id with values
    gcm_test.send_gcm_notif(regid, header, content)
    print(regid)
    return Response(json.dumps(a),  mimetype='application/json')