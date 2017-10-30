from flask import Flask,make_response,jsonify,g

app = Flask(__name__,static_url_path='/pethub/static')

app.config['SQLALCHEMY_DATABASE_URI'] = "mysql+pymysql://root:123456@localhost:3306/pethub2?charset=utf8"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
app.config['VERSION']='v0.1'
app.config['SECRET_KEY']='very secret key'

