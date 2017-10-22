from flask import Flask,make_response,jsonify

app = Flask(__name__,static_url_path='/pethub/static')

app.config['SQLALCHEMY_DATABASE_URI'] = "mysql+pymysql://root:123456@localhost:3306/pethub"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
app.config['VERSION']='v0.1'