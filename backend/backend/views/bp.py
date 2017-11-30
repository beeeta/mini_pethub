from flask import Blueprint,render_template

bp = Blueprint('blue',__name__)

@bp.route('/')
def index():
    return render_template('index.html')

@bp.route('/login')
def login():
    return render_template('login.html')

@bp.route('/adoption')
def adoption():
    return render_template('adoption.html')