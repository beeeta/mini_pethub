from flask import Flask,make_response,jsonify

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = "mysql+pymysql://root:123456@localhost:3307/pethub"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True