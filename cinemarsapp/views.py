from flask import Blueprint, render_template, request, session, redirect, url_for, abort, flash
from .models import DVD,Genre, Order, Actor, dvd_genre_association, dvd_actor_association
from . import db
from sqlalchemy import or_
from .forms import CheckoutForm

import traceback
from random import randint
from datetime import datetime

bp = Blueprint('main', __name__)

@bp.route('/')
def index():

  drama = 18 
  thriller = 53
  family = 10751

  drama_dvd = db.session.query(DVD).join(dvd_genre_association).join(Genre).filter(Genre.id == drama).limit(3).all()
  thriller_dvd = db.session.query(DVD).join(dvd_genre_association).join(Genre).filter(Genre.id == thriller).limit(3).all()
  family_dvd = db.session.query(DVD).join(dvd_genre_association).join(Genre).filter(Genre.id == family).limit(3).all()
  
  return render_template('index.html', drama_dvd = drama_dvd, thriller_dvd=thriller_dvd, family_dvd=family_dvd)

@bp.route('/detail/<int:dvd_id>', methods=['GET','POST'])
def detail(dvd_id):
  dvd_detail = db.session.query(DVD).filter(DVD.id == dvd_id).one()
  return render_template('detail.html', dvd = dvd_detail)

@bp.route('/order', methods=['GET', 'POST'])
def add_order():  
    dvd_id = request.values.get('dvd_id')
    print(f"dvd: {dvd_id}")
    
    if 'order_id' in session.keys():
        order = db.session.scalar(db.select(Order).where(Order.id == session['order_id']))
    else:
        order = None
        
    if order is None:
        order = Order(status='added', firstname='', lastname='', email=str(randint(0,9999)), phone=str(randint(0,9999)), total_cost=0.00, date=datetime.now())
        try:
            db.session.add(order)
            db.session.commit()
            session['order_id'] = order.id
        except:
            traceback.print_exc()
            print("Order addition failed")
            order = None
    total_price = 0
    if order is not None:
        for dvd in order.dvds:
            total_price += dvd.price
    
    if dvd_id is not None and order is not None:
        dvd = db.session.scalar(db.select(DVD).where(DVD.id == dvd_id))
        try:
            order.dvds.append(dvd)
            for dvd in order.dvds:
                total_price += dvd.price
            order.total_cost = total_price
            db.session.commit()
        except:
            flash("You've already have this DVD in your basket!")
            return redirect(request.referrer)
        return redirect(url_for('main.add_order'))
    # order = db.session.query(DVD).filter(DVD.id == dvd_id).one()
    return render_template('basket.html', order=order, total_price = total_price)

@bp.route('/remove-orderitem', methods=['GET','POST'])
def remove_orderitem():
    id = request.values.get('id')
    print(f"Id for dvd to remove is: {id}")
    
    if 'order_id' in session:
        order = db.session.scalar(db.select(Order).where(Order.id == session['order_id']))
        if not order:
            flash('There is no DVD to remove from your basket!')
        
        dvd_to_remove = db.session.scalar(db.select(DVD).where(DVD.id == id))
        print(f"Removing {dvd_to_remove.title}")
        
        try:
            order.dvds.remove(dvd_to_remove)
            db.session.commit()
        except:
            print("error occured while removing order item")
            abort(500)
    return redirect(url_for('main.add_order'))

@bp.route('/empty-order')
def empty_order():
    if 'order_id' in session:
        order = db.session.scalar(db.select(Order).where(Order.id == session['order_id']))
        for dvd in order.dvds:
            order.dvds.remove(dvd)
        session.pop('order_id')
        db.session.commit()
        flash("We've emptied your basket!")
    else:
        print("There is no order to empty out!")
        return redirect(request.referrer)
    return redirect(url_for('main.add_order'))

@bp.route('/checkout', methods=['GET', 'POST'])
def checkout_order():
    
    form = CheckoutForm()
    
    if 'order_id' in session:
        order = db.session.scalar(db.select(Order).where(Order.id == session['order_id']))
        if not order.dvds:
            return redirect(url_for(request.referrer))
        if form.validate_on_submit():
            order.status = 'checkedout'
            order.firstname = form.firstname.data
            order.lastname = form.lastname.data
            order.phone = form.phone.data
            order.email = form.email.data
            total_cost = 0
            for dvd in order.dvds:
                total_cost += dvd.price
            order.total_cost = total_cost
            order.date = datetime.now()
            
            try:
                db.session.commit()
                empty_order()
                flash('Thank you for your purchase! One of our team members will contact you via email soon.')
            except:
                flash('The error has occured while checking your order out!')
            
    return render_template('checkout.html', form=form) 

@bp.route('/dvds_all/<string:category>')
def get_dvd_all(category):
  dvd = {}
  if category == 'movie':
    dvd = db.session.scalars(db.select(DVD).where(DVD.category == 'movie'))
  if category == 'series':
    dvd = db.session.scalars(db.select(DVD).where(DVD.category == 'series'))  
  return render_template('dvd_all.html', dvd=dvd)

@bp.route('/search/genres/<int:genre_id>')
def get_dvd_by_genres(genre_id):
    
  dvd = db.session.query(DVD).join(dvd_genre_association).join(Genre).filter(Genre.id == genre_id).all()
  
  return render_template('dvd_all.html', dvd=dvd)

@bp.route('/search', methods=["GET", "POST"])
def search_dvd():
  search_query = f"%{request.args.get('search')}%"
  
  dvd = (
        db.session.query(DVD)
        .outerjoin(dvd_actor_association)
        .outerjoin(Actor)
        .outerjoin(dvd_genre_association)
        .outerjoin(Genre)
        .filter(
            or_(
                DVD.title.like(search_query),
                DVD.description.like(search_query),
                DVD.original_title.like(search_query),
                Actor.name.like(search_query),
                Genre.name.like(search_query)
            )
        )
        .all()
    )   
  return render_template('dvd_all.html', dvd=dvd)