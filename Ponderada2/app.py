from flask import Flask,render_template,request,redirect, abort, jsonify, make_response
from models import db,TextModel,UserModel, create_table
from flask_jwt_extended import JWTManager, jwt_required, create_access_token
import os

app = Flask(__name__)

app.config["JWT_SECRET_KEY"] = "Pablinho"
app.config["JWT_TOKEN_LOCATION"] = ["cookies"]
app.config["JWT_COOKIE_SECURE"] = False
app.config['JWT_COOKIE_CSRF_PROTECT'] = False
jwt = JWTManager(app)

app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql://postgres:password@db:5432/postgres"
#app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///"

db.init_app(app)

create_table(app)

@app.before_first_request
def create_table():
    db.create_all()
    db.session.add(UserModel(username=os.environ.get("USERNAME"), password=os.environ.get("PASSWORD")))
    db.session.commit()

@app.route('/', methods=['GET', 'POST'])
def Login():
    if request.method == 'GET':
        return render_template('index.html')

    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        user = UserModel.query.filter_by(username=username, password=password).first()
        if not user:
            return jsonify({"msg": "Bad username or password"}), 401
        access_token = create_access_token(identity=username)
        response = make_response(jsonify({"access_token": access_token}), 200)
        response.set_cookie('access_token_cookie', access_token, httponly=True)
        response.headers['Location'] = '/read'
        response.status_code = 302
        return response
    
@app.route('/read')
@jwt_required()
def RetrieveList():
    infos = TextModel.query.all()
    return render_template('read.html',infos = infos)

@app.route('/create' , methods = ['GET','POST'])
@jwt_required()
def create():
    if request.method == 'GET':
        return render_template('create.html')

    if request.method == 'POST':
        texto = request.form['texto']
        info = TextModel(texto=texto)
        db.session.add(info)
        db.session.commit()
        return redirect('/read')

@app.route('/update/<int:id>',methods = ['GET','POST'])
@jwt_required()
def update(id):
    info = TextModel.query.filter_by(id=id).first()
    if request.method == 'POST':
        if info:
            db.session.delete(info)
            db.session.commit()
            texto = request.form['texto']
            info = TextModel(texto=texto)
            db.session.add(info)
            db.session.commit()
            return redirect('/read')
        return f"info with id = {id} Does nit exist"
    return render_template('update.html', info = info)

@app.route('/delete/<int:id>', methods=['GET','POST'])
@jwt_required()
def delete(id):
    info = TextModel.query.filter_by(id=id).first()
    if request.method == 'POST':
        if info:
            db.session.delete(info)
            db.session.commit()
            return redirect('/read')
        abort(404)
    return render_template('delete.html')

app.run(host='0.0.0.0', port=4000, debug=True)