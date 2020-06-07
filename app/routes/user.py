from flask import Blueprint, render_template

bp_user = Blueprint('user', __name__)


@bp_user.route('/user/<string:username>')
def user_index(username):
    return render_template("user/user_index.html", username=username)


@bp_user.route('/user/<string:username>/register')
def user_register(username):
    return render_template("user/register.html", username=username)


@bp_user.route('/user/<string:username>/register_purchase')
def user_register_purchase(username):
    return render_template("user/register_purchase.html", username=username)


@bp_user.route('/user/<string:username>/treatment_purchase')
def user_treatment_purchase(username):
    return render_template("user/treatment_purchase.html", username=username)


@bp_user.route('/user/<string:username>/department')
def department(username):
    return render_template("manager/department.html", username=username)


@bp_user.route('/user/<string:username>/doctor')
def doctor(username):
    return render_template("manager/doctor.html", username=username)


@bp_user.route('/user/<string:username>/drugs')
def drugs(username):
    return render_template("manager/drugs.html", username=username)
