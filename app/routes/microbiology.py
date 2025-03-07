from flask import Blueprint, render_template, request, redirect, url_for, flash

microbiology = Blueprint('microbiology', __name__, url_prefix='/microbiology')

@microbiology.route('/')
def lab_info():
    return render_template('microbiology/lab_info.html') 