from . import db

class DVD (db.Model):
  __tablename__ = "dvds"
  id = db.Column(db.Integer, primary_key=True)
  title = db.Column(db.String(128), unique= True, nullable = False)
  original_title = db.Column(db.String(128), unique=True, nullable = False)
  genres = db.relationship("Genre", backref="Genre")
  genres_id = db.Column(db.Integer, db.ForeignKey('genres.id'))
  category = db.Column(db.String(64), nullable=False)
  adult = db.Column(db.Boolean, nullable=False)
  description = db.Column(db.String(255), nullable = False)
  background_image = db.Column(db.String(255))
  poster_image = db.Column(db.String(255))
  release_date = db.Column(db.DateTime, nullable = False)
  rating = db.Column(db.Float, nullable = False)
  price = db.Column(db.Float, nullable = False)
  # only for movies
  runtime = db.Column(db.Integer, default=0)
  # only for series
  episodes = db.Column(db.Integer, default=0)
  main_actors = db.relationship("Actor", backref="DVD")
  actors_id = db.Column(db.Integer, db.ForeignKey('actors.id'))
  to_wishlist = db.Column(db.Integer, db.ForeignKey('wishlists.id'))
  
# 14 = Fantasy, 18 = Drama, 28 = Action,  35 = Comedy, 80 = Crime, Family = , 53 = Thriller, 10749 = Romance, 10752 = War
dvd_genre_association = db.Table(
    'dvd_genre',
    db.Column('dvd_id', db.Integer, db.ForeignKey('dvds.id'), primary_key=True),
    db.Column('genre_id', db.Integer, db.ForeignKey('genres.id'), primary_key=True)
)

class Genre (db.Model):
  __tablename__ = 'genres'
  id = db.Column(db.Integer, primary_key=True)
  name = db.Column(db.String(128), unique = True, nullable = False)

dvd_actor_association = db.Table(
    'dvd_actor',
    db.Column('dvd_id', db.Integer, db.ForeignKey('dvds.id'), primary_key=True),
    db.Column('actor_id', db.Integer, db.ForeignKey('actors.id'), primary_key=True)
)

class Actor (db.Model):
  __tablename__ = 'actors'
  id = db.Column(db.Integer, primary_key=True)
  name = db.Column(db.String(64), unique = True, nullable = False)

order_detail = db.Table('order_detail', 
                        db.Column('order_id', db.Integer, db.ForeignKey('orders.id'), nullable=False),
                        db.Column('dvd_id', db.Integer, db.ForeignKey('dvds.id'), nullable=False),
                        db.PrimaryKeyConstraint('order_id', 'dvd_id')
                       )
  
class Order (db.Model):
  __tablename__ = 'orders'
  id = db.Column(db.Integer, primary_key=True)
  status = db.Column(db.String, nullable=False)
  firstname = db.Column(db.String(64), nullable=False)
  lastname = db.Column(db.String(64), nullable=False)
  email = db.Column(db.String(128), unique=True, nullable=False)
  phone = db.Column(db.String(32), unique=True, nullable=False)
  total_cost = db.Column(db.Float)
  date = db.Column(db.DateTime)
  dvds = db.relationship("DVD", secondary=order_detail, backref='orders')

inquiry_order_association = db.Table(
    'inquiry_detail',
    db.Column('order_id', db.Integer, db.ForeignKey('orders.id'), primary_key=True),
    db.Column('inquiry_id', db.Integer, db.ForeignKey('inquiries.id'), primary_key=True)
)

class Inquiry(db.Model):
    __tablename__ = 'inquiries'

    id = db.Column(db.Integer, primary_key=True)
    inquiry_date_time = db.Column(db.DateTime, nullable=False)
    content = db.Column(db.String(255), nullable=False)

    # Relationship with Order through InquiryDetail association table
    orders = db.relationship('Order', secondary=inquiry_order_association, backref='inquiries')

class Wishlist(db.Model):
    __tablename__ = 'wishlists'
    id = db.Column(db.Integer, primary_key=True)
    # Relationship to DVD
    dvds = db.relationship('DVD')
    

# Define additional relationships as necessary
  
# from sqlalchemy import Column, String, Float, Integer, DateTime, Boolean, ForeignKey, Table
# from sqlalchemy.orm import relationship
# from sqlalchemy.ext.declarative import declarative_base

# Base = declarative_base()

# # Association tables for many-to-many relationships
# order_dvd_association = Table(
#     'OrderDetail', Base.metadata,
#     Column('orderId', String, ForeignKey('order.orderId'), primary_key=True),
#     Column('dvdId', String, ForeignKey('dvd.dvdId'), primary_key=True)
# )

# inquiry_order_association = Table(
#     'InquiryDetail', Base.metadata,
#     Column('orderId', String, ForeignKey('order.orderId'), primary_key=True),
#     Column('inquiryId', String, ForeignKey('inquiry.inquiryId'), primary_key=True)
# )

# dvd_genre_association = Table(
#     'DVDGenre', Base.metadata,
#     Column('dvdId', String, ForeignKey('dvd.dvdId'), primary_key=True),
#     Column('genreId', String, ForeignKey('genre.genreId'), primary_key=True)
# )

# # Models based on the diagram with Genre added

# class DVD(Base):
#     __tablename__ = 'dvd'

#     dvdId = Column(String, primary_key=True)
#     title = Column(String, nullable=False)
#     director = Column(String)
#     actors = Column(String)  # Could also be a JSON field for an array of actors
#     image_urls = Column(String)  # Could be JSON for multiple image URLs
#     price = Column(Float, nullable=False)
#     rating = Column(Float)
#     overview = Column(String)
#     release_date = Column(DateTime)
#     runtime = Column(Integer)
#     inStock = Column(Boolean, default=True)

#     # Relationship to Order through the OrderDetail association table
#     orders = relationship('Order', secondary=order_dvd_association, back_populates='dvds')

#     # Relationship to Genre through the DVDGenre association table
#     genres = relationship('Genre', secondary=dvd_genre_association, back_populates='dvds')
    
#     # Relationship to Actor through DVDActor association table
#     actors = relationship('Actor', secondary=dvd_actor_association, back_populates='dvds')


# class Genre(Base):
#     __tablename__ = 'genre'

#     genreId = Column(String, primary_key=True)
#     name = Column(String, nullable=False, unique=True)
#     category = Column(String, nullable=False)

#     # Relationship to DVD through the DVDGenre association table
#     dvds = relationship('DVD', secondary=dvd_genre_association, back_populates='genres')

# class Actor(Base):
#     __tablename__ = 'actor'

#     actorId = Column(String, primary_key=True)
#     name = Column(String, nullable=False)

#     # Relationship to DVD through DVDActor association table
#     dvds = relationship('DVD', secondary=dvd_actor_association, back_populates='actors')

# class Order(Base):
#     __tablename__ = 'order'

#     orderId = Column(String, primary_key=True)
#     firstName = Column(String, nullable=False)
#     lastName = Column(String, nullable=False)
#     email = Column(String, nullable=False)
#     phoneNumber = Column(String)
#     orderDateTime = Column(DateTime, nullable=False)
#     estimatedTimeArrival = Column(Integer)
#     totalPrice = Column(Float, nullable=False)

#     # Relationship to DVD through the OrderDetail association table
#     dvds = relationship('DVD', secondary=order_dvd_association, back_populates='orders')

#     # Relationship with Inquiry through InquiryDetail association table
#     inquiries = relationship('Inquiry', secondary=inquiry_order_association, back_populates='orders')

# class Inquiry(Base):
#     __tablename__ = 'inquiry'

#     inquiryId = Column(String, primary_key=True)
#     inquiryDateTime = Column(DateTime, nullable=False)
#     content = Column(String, nullable=False)

#     # Relationship with Order through InquiryDetail association table
#     orders = relationship('Order', secondary=inquiry_order_association, back_populates='inquiries')

# class Wishlist(Base):
#     __tablename__ = 'wishlist'

#     id = Column(Integer, primary_key=True)
#     # Relationship to DVD
#     dvds = relationship('DVD')

# # Define additional relationships as necessary