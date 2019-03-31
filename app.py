import os
from flask import Flask
from flask_restful import Api
from flask_jwt import JWT
from security import authenticate, identity
from resources.user import UserRegister
from resources.item import Item, ItemList
#reqparse for parsing the requests, so not all data has to be read and posted each time
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL','sqlite:///data.db') #environment variable, default variabe (if environment failed)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.secret_key = 'pupsiusOPx'
api = Api(app)
app.config['PROPAGATE_EXCEPTIONS'] = True # To allow flask propagating exception even if debug is set to false on app
jwt = JWT(app, authenticate, identity) # creates /auth endpoint




api.add_resource(Item, '/item/<string:name>')
api.add_resource(ItemList, '/items')
api.add_resource(UserRegister, '/register')

if __name__ == '__main__':
	from db import db
	db.init_app(app)
	app.run(port=5000, debug=True)