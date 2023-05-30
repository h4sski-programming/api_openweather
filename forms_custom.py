from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, Length


class FormCity(FlaskForm):
    city = StringField('Type city name', validators=[DataRequired(), Length(3, 30)])
    country_code = StringField('Type country code [only 2 letters]', validators=[DataRequired(), Length(2)])
    submit = SubmitField('Show weather')
