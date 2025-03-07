from flask import Blueprint, render_template, request, redirect, url_for, flash

chemistry = Blueprint('chemistry', __name__, url_prefix='/chemistry')

@chemistry.route('/')
def lab_info():
    return render_template('chemistry/lab_info.html') 