from flask import Blueprint, render_template, request, redirect, url_for, flash
from app.forms.forms import CompanyRegistrationForm, TruckAppointmentForm

metrology = Blueprint('metrology', __name__, url_prefix='/metrology')

@metrology.route('/register_company', methods=['GET', 'POST'])
def register_company():
    form = CompanyRegistrationForm()
    if form.validate_on_submit():
        # Process the registration (placeholder functionality)
        flash('Company registration submitted successfully! Pending verification.', 'success')
        return redirect(url_for('metrology.register_company'))
    return render_template('metrology/register_company.html', form=form)

@metrology.route('/schedule_appointment', methods=['GET', 'POST'])
def schedule_appointment():
    form = TruckAppointmentForm()
    if form.validate_on_submit():
        # Process the appointment scheduling (placeholder functionality)
        flash('Appointment scheduled successfully!', 'success')
        return redirect(url_for('metrology.schedule_appointment'))
    return render_template('metrology/schedule_appointment.html', form=form) 