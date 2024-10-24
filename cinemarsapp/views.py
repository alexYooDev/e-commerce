from flask import Blueprint, render_template
# from .models import DVD

bp = Blueprint('main', __name__)

@bp.route('/')
def index():
  return render_template('index.html')

@bp.route('/detail')
def detail():
  return render_template('detail.html')