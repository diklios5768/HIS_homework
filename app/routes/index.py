from flask import Blueprint, render_template, session, redirect, url_for

bp_idx = Blueprint('index', __name__)


@bp_idx.route('/')
@bp_idx.route('/index')
def index():
    return render_template("index.html")


@bp_idx.route('/login')
def login():
    if session['logged_in']:
        user_name = session['name']
        if session['identity'] == 'user':
            return redirect(url_for('bp_user.user_index', name=user_name))
        else:
            return redirect(url_for('bp_manager.manager_index', name=user_name))
    else:
        return render_template("login.html")


@bp_idx.route('/login_confirm')
def login_confirm():
    # data = request.args()

    return ""


@bp_idx.route('/signup')
def signup():
    return render_template("signup.html")
