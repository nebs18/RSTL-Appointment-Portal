from flask import Blueprint, render_template, request, redirect, url_for, flash

admin = Blueprint('admin', __name__, url_prefix='/admin/metrology')

@admin.route('/dashboard')
def dashboard():
    return render_template('admin/dashboard.html')

@admin.route('/verify_company', methods=['GET', 'POST'])
def verify_company():
    return render_template('admin/verify_company.html') 