from flask import Blueprint, render_template

bp_manager = Blueprint('manager', __name__)


@bp_manager.route('/manage/<string:name>')
def manager_index(name):
    return render_template("manager/manager_index.html")
