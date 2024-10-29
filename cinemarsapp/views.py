from flask import Blueprint, render_template, request, session, redirect, url_for, abort, flash
from .models import DVD,Genre, Order, Actor, Wishlist, User, dvd_genre_association, dvd_actor_association
from . import db
from sqlalchemy import or_
from .forms import CheckoutForm

import traceback
from random import randint
from datetime import datetime

bp = Blueprint('main', __name__)

# Present view for the main landing page of the store, with 3 popular genres of dvd
@bp.route('/')
def index():

  drama = 18 
  thriller = 53
  family = 10751

  drama_dvd = db.session.query(DVD).join(dvd_genre_association).join(Genre).filter(Genre.id == drama).limit(3).all()
  thriller_dvd = db.session.query(DVD).join(dvd_genre_association).join(Genre).filter(Genre.id == thriller).limit(3).all()
  family_dvd = db.session.query(DVD).join(dvd_genre_association).join(Genre).filter(Genre.id == family).limit(3).all()
  
  return render_template('index.html', drama_dvd = drama_dvd, thriller_dvd=thriller_dvd, family_dvd=family_dvd)

# Route to detail page with dvd detail view
@bp.route('/detail/<int:dvd_id>', methods=['GET','POST'])
def detail(dvd_id):
  dvd_detail = db.session.query(DVD).filter(DVD.id == dvd_id).one()
  return render_template('detail.html', dvd = dvd_detail)

#  Controller for adding dvd to order and present order page view
@bp.route('/order', methods=['GET', 'POST'])
def add_order():  
    dvd_id = request.values.get('dvd_id')
    
    if 'order_id' in session.keys():
        order = db.session.scalar(db.select(Order).where(Order.id == session['order_id']))
    else:
        order = None
        
    if order is None:
        user = User(first_name='', last_name='', email=str(randint(0,9999)), phone=str(randint(0,9999)))
        order = Order(status=False, total_cost=0.00, date=datetime.now())
        try:
            db.session.add(user)
            db.session.add(order)
            db.session.commit()
            session['order_id'] = order.id
            session['user_id'] = user.id
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
    return render_template('basket.html', order=order, total_price = total_price)

#  Removing dvd order item from order page view 
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

# empty out all dvd order items from order page view
@bp.route('/empty-order')
def empty_order():
    if 'order_id' in session:
        order = db.session.scalar(db.select(Order).where(Order.id == session['order_id']))
        for dvd in order.dvds:
            order.dvds.remove(dvd)
        session.pop('order_id')
        db.session.commit()
    else:
        print("There is no order to empty out!")
        return redirect(request.referrer)
    return redirect(url_for('main.add_order'))

# Present view to the checkout Form and allow user order detail submission
@bp.route('/checkout', methods=['GET', 'POST'])
def checkout_order():
    
    form = CheckoutForm()
    
    if 'order_id' in session:
        order = db.session.scalar(db.select(Order).where(Order.id == session['order_id']))
        if not order.dvds:
            return redirect(url_for(request.referrer))
        if form.validate_on_submit():
            order.status = True
            order.user.first_name = form.firstname.data
            order.user.last_name = form.lastname.data
            order.user.phone = form.phone.data
            order.user.email = form.email.data
            total_cost = 0
            for dvd in order.dvds:
                total_cost += dvd.price
            order.total_cost = total_cost
            order.date = datetime.now()
            
            try:
                db.session.commit()
                empty_order()
                flash('Thank you for your purchase! We will send you shipment detail via email soon.')
            except:
                flash('The error has occured while checking your order out!')
            
    return render_template('checkout.html', form=form, order=order.dvds) 

#  Get recommended dvds and present in main page view
@bp.route('/dvds/<string:category>')
def get_dvds(category):
  dvd = {}
  if category == 'movie':
    dvd = db.session.scalars(db.select(DVD).where(DVD.category == 'movie'))
  if category == 'series':
    dvd = db.session.scalars(db.select(DVD).where(DVD.category == 'series'))  
  if category == 'intl':
    dvd = db.session.scalars(db.select(DVD).where(DVD.original_title != DVD.title))
  return render_template('dvds.html', dvd=dvd)

# Allow filter for different dvd genres and present in DVDs page
@bp.route('/search/dvds/genres/<int:genre_id>')
def get_dvds_by_genres(genre_id):
    
  dvd = db.session.query(DVD).join(dvd_genre_association).join(Genre).filter(Genre.id == genre_id).all()
  
  return render_template('dvds.html', dvd=dvd)

# Add wishlist items to wish list and present them in My Wishlist page
@bp.route('/add-wishlist-item', methods=["GET", "POST"])
def add_wishlist():
    dvd_id = request.values.get('dvd_id')
    if 'wishlist_id' in session:
        wishlist_item = db.session.scalar(db.select(Wishlist).where(Wishlist.id == session['wishlist_id']))
    else:
        wishlist_item = None
        
    if 'user_id' in session:
        user = db.session.scalar(db.select(User).where(User.id == session['user_id']))
    else:
        user = User(first_name='', last_name='', email=str(randint(0,9999)), phone=str(randint(0,9999)))
        db.session.add(user)
        db.session.commit()
        
    if wishlist_item is None:
        wishlist_item = Wishlist(user_id = user.id)
        try:
            db.session.add(wishlist_item)
            db.session.commit()
            session['wishlist_id'] = wishlist_item.id
        except:
            traceback.print_exc()
            flash("Wishlist creation failed.")
            return redirect(url_for('main.add_wishlist'))

    if dvd_id is not None and wishlist_item is not None:
        dvd = db.session.scalar(db.select(DVD).where(DVD.id == dvd_id))
        if dvd is not None:
            if dvd not in wishlist_item.dvds:
                wishlist_item.dvds.append(dvd)
                db.session.commit()
            else:
                flash("You've already added this DVD to your wishlist!")
                return redirect(request.referrer)
        else:
            flash("DVD not found.")
            return redirect(request.referrer)

    return render_template('wishlist.html', wishlist=wishlist_item.dvds)

# Remove wishlist item view from My Wishlist page
@bp.route('/remove-wishlist-item', methods=['GET','POST'])
def remove_wishlist_item():
    wishlist_item_id = request.values.get('id')
    
    if 'wishlist_id' in session:
        wishlist = db.session.scalar(db.select(Wishlist).where(Wishlist.id == session['wishlist_id']))
        
        if not wishlist:
            flash('There is no DVD to remove from your wishlist!')
        print(f"dvd id: {DVD.id} | wish item id : {wishlist_item_id}")
        dvd_to_remove = db.session.scalar(db.select(DVD).where(DVD.id == wishlist_item_id))
        print(f"Removing {dvd_to_remove}")
        
        try:
            wishlist.dvds.remove(dvd_to_remove)
            db.session.commit()
        except:
            print("error occured while removing wishlist item")
            abort(500)
    return redirect(url_for('main.add_wishlist')) 
  
# Dynamic search by DVD title, parts of detail description, original title for foreign language title, directors, actors, and genres
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
                DVD.director.like(search_query),
                Actor.name.like(search_query),
                Genre.name.like(search_query)
            )
        )
        .all()
    )   
  return render_template('dvds.html', dvd=dvd)