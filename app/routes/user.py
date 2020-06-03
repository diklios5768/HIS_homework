from flask import Blueprint, render_template

bp_user = Blueprint('user', __name__)


@bp_user.route('/<string:name>')
def user_index():
    return render_template("user/user_index.html")
