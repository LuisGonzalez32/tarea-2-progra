from flask import Blueprint, render_template, redirect, url_for
from flask_login import current_user, login_required
from forms.orderDetailCreateForm import OrderDetailCreateForm
from utils.db import db
from models.order import Order
from models.orderdetail import OrderDetail

orderDetails = Blueprint("orderDetails", __name__, url_prefix="/orderDetails")


@orderDetails.route("/")
@login_required
def home():
    return render_template("orderDetails/home.html")


@orderDetails.route("/create", methods=["GET", "POST"])
@login_required
def create():
    form = OrderDetailCreateForm()
    if form.validate_on_submit():
        orderId = form.orderId.data
        # currentOrder = Order.query.filter_by(id=orderId)
        quantity = form.quantity.data
        description = form.description.data
        unitCost = form.unitCost.data
        totalCost = quantity * unitCost
        currentOrder.TotalSale += totalCost
        db.session.add(currentorder)
        newOrderDetail = OrderDetail(orderId, quantity, description, unitCost, totalCost)
        db.session.add(newOrderDetail)
        db.session.commit()
        return redirect(url_for("orderDetails.home"))
    return render_template("orderDetails/create.html", form=form)
