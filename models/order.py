from utils.db import db
from datetime import datetime


class Order(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    buyer = db.Column(db.String(50), nullable=False)
    provider = db.Column(db.String(50), nullable=False)
    date = db.Column(db.DateTime(), nullable=False)
    totalSale = db.Column(db.Integer, nullable=False)
    discount = db.Column(db.Integer, nullable=False)
    tax = db.Column(db.Integer, nullable=False)

    def __init__(self, buyer, provider, totalSale, discount, tax) -> None:
        self.buyer = buyer
        self.provider = provider
        self.totalSale = totalSale
        self.date = datetime.now()
        self.discount = discount
        self.tax = tax

    def __repr__(self) -> str:
        return f"Order({self.id}, {self.buyer}, '{self.provider}', '{self.totalSale}', '{self.date}', '{self.discount}', '{self.tax}')"
