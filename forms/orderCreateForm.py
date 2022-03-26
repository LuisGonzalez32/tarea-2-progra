from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, IntegerField
from wtforms.validators import InputRequired, Length, ValidationError
from wtforms.fields import DateField
from models.user import User


class OrderCreateForm(FlaskForm):
    buyer = StringField(
        validators=[
            InputRequired(),
            Length(min=3, max=20),
        ],
        render_kw={"placeholder": "buyer"},
    )

    totalSale = IntegerField(
        validators=[
            InputRequired(),
        ],
        render_kw={"placeholder": "total"},
    )

    discount = IntegerField(
        validators=[
            InputRequired(),
        ],
        render_kw={"placeholder": "discount"},
    )

    tax = IntegerField(
        validators=[
            InputRequired(),
        ],
        render_kw={"placeholder": "tax"},
    )

    submit = SubmitField("create")
