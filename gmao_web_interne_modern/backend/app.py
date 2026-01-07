
from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS

app = Flask(__name__)
CORS(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///gmao.db'
db = SQLAlchemy(app)

class Equipement(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nom = db.Column(db.String(100))
    localisation = db.Column(db.String(100))

@app.route('/api/equipements', methods=['GET','POST'])
def equipements():
    if request.method == 'POST':
        e = Equipement(nom=request.json['nom'], localisation=request.json['localisation'])
        db.session.add(e)
        db.session.commit()
    return jsonify([{"id":e.id,"nom":e.nom,"localisation":e.localisation} for e in Equipement.query.all()])

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run()
