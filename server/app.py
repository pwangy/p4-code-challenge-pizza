#!/usr/bin/env python3
from models import db, Restaurant, RestaurantPizza, Pizza
from flask_restful import Api, Resource
from flask_migrate import Migrate
from flask import Flask, request, make_response
import os

BASE_DIR = os.path.abspath(os.path.dirname(__file__))
DATABASE = os.environ.get("DB_URI", f"sqlite:///{os.path.join(BASE_DIR, 'app.db')}")

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = DATABASE
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.json.compact = False

migrate = Migrate(app, db)
db.init_app(app)
api = Api(app)


@app.route("/")
def index():
    return "<h1>The Pizza Society</h1>"


class Restaurants(Resource):
    def get(self):
        pass


api.add_resource(Restaurants, "/restaurants")


class RestaurantsById(Resource):
    def get(self, id):
        pass

    def delete(self, id):
        pass

api.add_resource(RestaurantsById, "/restaurants/<int:id>")


class Pizzas(Resource):
    def get(self):
        pass


api.add_resource(Pizzas, "/pizzas")


class RestaurantPizzas(Resource):
    def get(self):
        pass


api.add_resource(RestaurantPizzas, "/restaurant_pizzas")


if __name__ == "__main__":
    app.run(port=5555, debug=True)
