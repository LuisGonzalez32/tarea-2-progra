from flask import Blueprint, render_template, redirect, url_for
from flask_login import current_user, login_required
from utils.db import db

store = Blueprint("store", __name__, url_prefix="/store")


@store.route("/")
@login_required
def home():
    return render_template("store/home.html", user=current_user)
