from flask import Flask,render_template,request,redirect, abort
from models import db,TextModel

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)

@app.before_first_request
def create_table():
    db.create_all()

@app.route('/data/create' , methods = ['GET','POST'])
def create():
    if request.method == 'GET':
        return render_template('create.html')

    if request.method == 'POST':
        texto = request.form['texto']
        info = TextModel(texto=texto)
        db.session.add(info)
        db.session.commit()
        return redirect('/data')


@app.route('/data')
def RetrieveList():
    infos = TextModel.query.all()
    return render_template('read.html',infos = infos)


@app.route('/data/<int:id>/update',methods = ['GET','POST'])
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
            return redirect(f'/data')
        return f"info with id = {id} Does nit exist"

    return render_template('update.html', info = info)


@app.route('/data/<int:id>/delete', methods=['GET','POST'])
def delete(id):
    info = TextModel.query.filter_by(id=id).first()
    if request.method == 'POST':
        if info:
            db.session.delete(info)
            db.session.commit()
            return redirect('/data')
        abort(404)

    return render_template('delete.html')

app.run(host='localhost', port=5000, debug=True)