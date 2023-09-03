from sqlalchemy import Column, Integer, String, MetaData, ForeignKey
from sqlalchemy.orm import relationship, backref
from sqlalchemy.ext.declarative import declarative_base

convention = {
    "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",
}
metadata = MetaData(naming_convention=convention)

Base = declarative_base(metadata=metadata)

class Customer(Base):
    __tablename__ = "customers"
    id = Column(Integer(), primary_key=True)
    first_name =  Column(String(), nullable=False)
    last_name:  Column(String(), nullable=False)
    reviews: relationship("Review", backref=backref('customer'))
    restaurants = relationship("Restaurant", secondary="reviews", back_populates="customers")

    def __repr__(self):
        return f"<Customer first_name={self.first_name} last_name={self.last_name}>"
    


class Restaurant(Base):
    __tablename__ = "restaurants"
    id = Column(Integer(), primary_key=True)
    name = Column(String(), nullable=False)
    price = Column(String(), nullable=False)
    reviews = relationship("Review", backref=backref('restaurant'))
    customers = relationship("Customer", secondary="reviews", back_populates="restaurants")

    def __repr__(self):
        return f"<Restaurant name={self.name} price={self.price}>"
    

class Review(Base):
    __tablename__ = "reviews"
    id = Column(Integer(), primary_key=True)
    star_rating = Column(Integer(), nullable=False)
    customer_id = Column(Integer(), ForeignKey('customers.id'), nullable=False)
    restaurant_id = Column(Integer(), ForeignKey('restaurants.id'), nullable=False)

    def __repr__(self):
        return f"<Review star_rating={self.star_rating}>"