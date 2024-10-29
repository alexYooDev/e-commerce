from . import db
from datetime import datetime

# Association tables for models" relationships
dvd_genre_association = db.Table(
    "dvd_genre",
    db.Column("dvd_id", db.Integer, db.ForeignKey("dvds.id"), primary_key=True),
    db.Column("genre_id", db.Integer, db.ForeignKey("genres.id"), primary_key=True)
)

dvd_actor_association = db.Table(
    "dvd_actor",
    db.Column("dvd_id", db.Integer, db.ForeignKey("dvds.id"), primary_key=True),
    db.Column("actor_id", db.Integer, db.ForeignKey("actors.id"), primary_key=True)
)

dvd_wishlist_association = db.Table(
    "wishlist_detail",
    db.Column("dvd_id", db.Integer, db.ForeignKey("dvds.id"), primary_key=True),
    db.Column("wishlist_id", db.Integer, db.ForeignKey("wishlists.id"), primary_key=True)
)

user_order_association = db.Table(
    "user_order",
    db.Column("order_id", db.Integer, db.ForeignKey("orders.id"), primary_key=True),
    db.Column("user_id", db.Integer, db.ForeignKey("users.id"), primary_key=True)
)


order_dvd_association = db.Table("order_dvd_association", 
    db.Column("order_id", db.Integer, db.ForeignKey("orders.id"), nullable=False),
    db.Column("dvd_id", db.Integer, db.ForeignKey("dvds.id"), nullable=False),
    db.PrimaryKeyConstraint("order_id", "dvd_id")
)

class DVD(db.Model):
    __tablename__ = "dvds"
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(128), unique=True, nullable=False)
    original_title = db.Column(db.String(128), nullable=False)
    description = db.Column(db.String(255), nullable=False)
    background_image = db.Column(db.String(255))
    poster_image = db.Column(db.String(255))
    release_date = db.Column(db.Date)
    director = db.Column(db.String(128))
    rating = db.Column(db.Float, nullable=False)
    price = db.Column(db.Float, nullable=False)
    running_time = db.Column(db.Integer)
    category = db.Column(db.String(50))
    episodes = db.Column(db.Integer)
    in_stock = db.Column(db.Boolean, default=True)
    
    # Relationships
    genres = db.relationship("Genre", secondary=dvd_genre_association, back_populates="dvds")
    actors = db.relationship("Actor", secondary=dvd_actor_association, back_populates="dvds")
    wishlists = db.relationship("Wishlist", secondary=dvd_wishlist_association, back_populates="dvds")

# 14 = Fantasy, 18 = Drama, 28 = Action,  35 = Comedy, 80 = Crime, Family = , 53 = Thriller, 10749 = Romance, 10752 = War etc..
class Genre(db.Model):
    __tablename__ = "genres"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(128), unique=True, nullable=False)
    
    # Relationship to DVDs
    dvds = db.relationship("DVD", secondary=dvd_genre_association, back_populates="genres")

class Actor(db.Model):
    __tablename__ = "actors"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(128), unique=True, nullable=False)
    
    # Relationship to DVDs
    dvds = db.relationship("DVD", secondary=dvd_actor_association, back_populates="actors")

class User(db.Model):
    __tablename__ = "users"
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(64), nullable=False)
    last_name = db.Column(db.String(64), nullable=False)
    email = db.Column(db.String(128), unique=True, nullable=False)
    phone = db.Column(db.String(32), unique=True, nullable=True)
    address = db.Column(db.String(128), nullable=True)
    
    # Relationships
    wishlists = db.relationship("Wishlist", back_populates="user")
    orders = db.relationship("Order", secondary=user_order_association, back_populates="user")

class Order (db.Model):
    __tablename__ = "orders"
    id = db.Column(db.Integer, primary_key=True)
    status = db.Column(db.Boolean, default=False)
    total_cost = db.Column(db.Float)
    date = db.Column(db.DateTime)
    dvds = db.relationship("DVD", secondary=order_dvd_association, backref="orders")
    user = db.relationship("User", secondary=user_order_association, back_populates="orders")

class Wishlist(db.Model):
    __tablename__ = "wishlists"
    id = db.Column(db.Integer, primary_key=True)
    # Foreign key to User
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"), nullable=False)
    
    # Relationships
    dvds = db.relationship("DVD", secondary=dvd_wishlist_association, back_populates="wishlists")
    user = db.relationship("User", back_populates="wishlists")
    