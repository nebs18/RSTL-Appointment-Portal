from flask_wtf import FlaskForm
from wtforms import StringField, DecimalField, SubmitField, FileField, SelectField, DateField, TelField, EmailField, BooleanField
from wtforms.validators import DataRequired, NumberRange, InputRequired, Email


class CompanyRegistrationForm(FlaskForm):
    company_name = StringField('Company Name', validators=[DataRequired()])
    business_permit = FileField('Business Permit', validators=[DataRequired()])
    orcr = FileField('ORCR', validators=[DataRequired()])
    license_plate = StringField('License Plate', validators=[DataRequired()])
    submit = SubmitField('Register')


class TruckAppointmentForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired()])
    email = EmailField('Email', validators=[DataRequired(), Email()])
    contact_number = TelField('Contact Number', validators=[DataRequired()])
    service = SelectField('Service To Avail', choices=[
        ('', 'Select a service'),
        ('calibration', 'Calibration'),
        ('measurement', 'Measurement')
    ], validators=[DataRequired()])
    appointment_date = DateField('Appointment Date', validators=[DataRequired()])
    truck_license_plate = StringField('Truck License Plate', validators=[DataRequired()])
    liquid_carried = DecimalField('Liquid Carried (liters)', validators=[InputRequired(), NumberRange(min=0)], places=2)
    terms = BooleanField('Terms of Service', validators=[DataRequired()])
    confirm = BooleanField('Confirmation', validators=[DataRequired()]) 