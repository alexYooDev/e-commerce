from flask import Flask, render_template
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
import os 
from dotenv import load_dotenv

db = SQLAlchemy()

def create_app():
  app = Flask(__name__)
  
  app.debug = True
  app.secret_key = 'my_cinemars_secret_key'
  
  app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///cinemars.sqlite'
  
  # link db with app
  db.init_app(app)
  
  from . import views
  app.register_blueprint(views.bp)
  
  from . import admin
  app.register_blueprint(admin.bp)
  
  @app.errorhandler(404)
  def not_founed(error):
    return render_template('error.html', error=error)
  
  @app.errorhandler(500)
  def internal_error(error):
    return render_template('error.html', error=error)
  
  return app