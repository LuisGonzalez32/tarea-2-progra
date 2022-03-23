from flask import Blueprint, render_template, redirect, url_for
from flask_login import current_user, login_required
from forms.orderCreateForm import OrderCreateForm
from utils.db import db
from models.order import Order
from models.orderdetail import OrderDetail

orders = Blueprint("orders", __name__, url_prefix="/orders")


@orders.route("/")
@login_required
def ordersMain():
    orderList = Order.query.all()
    return render_template("orders/main.html", items=orderList, user=current_user)


@orders.route("/create", methods=["GET", "POST"])
@login_required
def create():
    form = OrderCreateForm()
    if form.validate_on_submit():
        buyer = form.buyer.data
        provider = form.provider.data
        orderCode = form.orderCode.data
        saleCode = form.saleCode.data
        newOrder = Order(buyer, provider, orderCode, saleCode)
        db.session.add(newOrder)
        db.session.commit()
        return redirect(url_for("orders.ordersMain"))
    return render_template("orders/create.html", form=form)
