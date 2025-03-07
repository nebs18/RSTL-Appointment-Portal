from flask_wtf import FlaskForm
from wtforms import StringField, DecimalField, SubmitField, FileField
from wtforms.validators import DataRequired, NumberRange, InputRequired


class CompanyRegistrationForm(FlaskForm):
    company_name = StringField('Company Name', validators=[DataRequired()])
    business_permit = FileField('Business Permit', validators=[DataRequired()])
    orcr = FileField('ORCR', validators=[DataRequired()])
    license_plate = StringField('License Plate', validators=[DataRequired()])
    submit = SubmitField('Register')


class TruckAppointmentForm(FlaskForm):
    truck_license_plate = StringField('Truck License Plate', validators=[DataRequired()])
    liquid_carried = DecimalField('Liquid Carried (liters)', validators=[InputRequired(), NumberRange(min=0)], places=2)
    submit = SubmitField('Schedule Appointment') 