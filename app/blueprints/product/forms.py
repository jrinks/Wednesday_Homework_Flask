from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, DecimalField
from wtforms.validators import DataRequired


class ProductForm(FlaskForm):
    name = StringField('Product Name')
    description = StringField('Product Description')
    price = DecimalField('Per Unit Price', places=2)
    image = StringField('Product Image URL')
    submit = SubmitField()


class DeletePostForm(FlaskForm):
    submit = SubmitField()