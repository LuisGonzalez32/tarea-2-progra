from flask import Blueprint, render_template, redirect, url_for
from flask_login import current_user, login_required
from forms.orderCreateForm import OrderCreateForm
from utils.db import db
from models.order import Order
from datetime import date

orders = Blueprint("orders", __name__, url_prefix="/orders")


@orders.route("/")
@login_required
def home():
    orderList = Order.query.all()
    return render_template("orders/home.html", items=orderList, user=current_user)


@orders.route("/create", methods=["GET", "POST"])
@login_required
def create():
    form = OrderCreateForm()
    if form.validate_on_submit():
        buyer = form.buyer.data
        provider = current_user.username
        total = form.totalSale.data
        discount = form.discount.data
        tax = form.tax.data
        total = total - (total * (discount/100))
        totalSale = total + (total * (tax/100))
        print(totalSale)
        newOrder = Order(buyer, provider, totalSale, discount, tax)
        db.session.add(newOrder)
        db.session.commit()
        return redirect(url_for("orders.home"))
    return render_template("orders/create.html", form=form)


@orders.route("/delete/<int:orderId>")
@login_required
def delete(orderId):
    currentOrder = Order.query.filter_by(id=orderId).first()
    db.session.delete(currentOrder)
    db.session.commit()
    return redirect(url_for("orders.home"))


