from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import MetaData
from sqlalchemy.orm import validates
from sqlalchemy.ext.associationproxy import association_proxy
from sqlalchemy_serializer import SerializerMixin

metadata = MetaData(
    naming_convention={
        "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",
    }
)

db = SQLAlchemy(metadata=metadata)

# A Restaurant has many Pizzas through RestaurantPizza
class Restaurant(db.Model, SerializerMixin):
    __tablename__ = "restaurants"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    address = db.Column(db.String)
    # add relationship
    restaurant_pizzas = db.relationship(
        "RestaurantPizza", back_populates="restaurant", cascade="all, delete orphan"
    )
    pizzas = association_proxy("restaurnat_pizzas", "pizza")

    # add serialization rules
    serialize_rules = ("-restaurant+pizzas.restaurant")

    def __repr__(self):
        return f"<Restaurant {self.name}>"


# A Pizza has many Restaurants through RestaurantPizza
class Pizza(db.Model, SerializerMixin):
    __tablename__ = "pizzas"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    ingredients = db.Column(db.String)
    # add relationship
    restaurant_pizzas = db.relationship(
        "RestaurantPizza", back_populates="pizza", cascade="all, delete orphan"
    )
    pizzas = association_proxy("restaurnat_pizzas", "restaurant")

    # add serialization rules
    serialize_rules = ("-restaurant_pizzas.pizza")

    def __repr__(self):
        return f"<Pizza {self.name}, {self.ingredients}>"


# A RestaurantPizza belongs to a Restaurant and belongs to a Pizza
class RestaurantPizza(db.Model, SerializerMixin):
    __tablename__ = "restaurant_pizzas"

    id = db.Column(db.Integer, primary_key=True)
    price = db.Column(db.Integer, nullable=False)
    restaurant_id = db.column(db.Integer, db.Foreignkey('restaurants.id'))
    pizza_id = db.column(db.Integer, db.Foreignkey('restaurants.id'))
    # add relationships
    restaurant = db.relationship("Restaurant", back_populates="restaurant_pizzas")
    pizza = db.relationship("Pizza", back_populates="restaurant_pizzas")

    # add serialization rules
    serialize_rules = ("-restaurant.restaurant_pizzas", "-pizza.restaurant_pizzas")

    # add validation

    def __repr__(self):
        return f"<RestaurantPizza ${self.price}>"
