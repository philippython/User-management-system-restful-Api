import datetime
import math
import uuid
import datetime
from flask import Flask, request, jsonify, redirect, render_template
import os
from dotenv import load_dotenv
from flask_sqlalchemy import SQLAlchemy
from flask_swagger_ui import get_swaggerui_blueprint
import requests

load_dotenv()

app = Flask(__name__)

database_user = os.getenv('DATABASE_USER')
database_password = os.getenv('DATABASE_PASSWORD')
database_host = os.getenv('DATABASE_HOST')
database_name = os.getenv('DATABASE_NAME')

postgresql_path =os.environ.get('DATABASE_URL', 'postgresql://{}:{}@{}/{}'.format(database_user, database_password, database_host, database_name))
app.config['SQLALCHEMY_DATABASE_URI'] = postgresql_path
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY')

SWAGGER_URL = '/swagger'
API_URL = '/static/swagger.json'
SWAGGER_BLUEPRINT = get_swaggerui_blueprint(
        SWAGGER_URL,
        API_URL,
        config={
            'app_name' : "User Management API"
        }
)

app.register_blueprint(SWAGGER_BLUEPRINT, url_prefix = SWAGGER_URL)

db = SQLAlchemy(app)

##############-------------------Models Creation-------------------####################


class Countries(db.Model):
    __tablename__ = 'countries'
    id = db.Column(db.Integer, primary_key=True)
    country_code = db.Column(db.String(80), nullable=False)
    country_name = db.Column(db.String(120), nullable=False)
    short_code = db.Column(db.String(80), nullable=False)

    users = db.relationship('Users', cascade='all, delete-orphan', backref='country', lazy=True)


class Users(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Text, default=lambda: str(uuid.uuid4()), unique=True)  # uuid field
    first_name = db.Column(db.String(80), nullable=False)
    last_name = db.Column(db.String(120), nullable=False)
    email = db.Column(db.String(80), unique=True, nullable=False)
    phone = db.Column(db.String(80), unique=True, nullable=False)
    sex = db.Column(db.String(80), nullable=False)
    status = db.Column(db.Boolean, nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.datetime.utcnow) # current time of creation
    updated_at = db.Column(db.DateTime, default=datetime.datetime.utcnow) # time of update(i.e patch request)
    country_id = db.Column(db.Integer, db.ForeignKey('countries.id', onupdate='cascade', ondelete='cascade'))
# all countries api url

ALL_COUNTRIES_URL = 'https://countriesnow.space/api/v0.1/countries/codes'

# db.create_all()


@app.route('/')
def home():
    return render_template('index.html')


# Populating the countries table


# response = requests.get(ALL_COUNTRIES_URL)
# data = response.json()
# country_data = data['data']

# for country in country_data:
#     new_country = Countries(country_code=country['code'], country_name=country['name'],
#                             short_code=country['dial_code'])
#     db.session.add(new_country)
#     db.session.commit()
# print('population completed')(


# app routes
@app.route('/add_user', methods=['POST'])
def add_user():
    user_country = request.form.get('country')
    email = request.form.get('email')
    print(email)
    user = db.session.query(Users).filter_by(email=email).first()
    print(user)

    if user:
        return jsonify(reponse={'error': f'User with {email} already exist'})
    else:

        country = db.session.query(Countries).filter_by(country_name=user_country).first()
        if country:
            new_user = Users(first_name=request.form.get('firstname'), last_name=request.form.get('lastname'),
                            email=request.form.get('email'), phone=request.form.get('phone'), sex=request.form.get('sex'),
                            status=True, country_id=country.id)
            db.session.add(new_user)
            db.session.commit()
            return jsonify(reponse={'msg': 'successfully added user to the database'})
        return jsonify(reponse={'error': f'Country name => {country} not found'})



@app.route('/all_users')
def all_users():
    page = request.args.get('page', 1, type=int)
    per_page = request.args.get('per_page', 5, type=int)
    country_id = request.args.get('country_id', type=int)

    users = db.session.query(Users).filter_by(country_id=country_id).all()

    total_pages = math.ceil(len(users) / per_page)

    if users:
        user_list = []
        for user in users:
            if user.status:
                user_list.append({
                                 'user_info':{
                                  'country_id': user.country_id,
                                  'uuid': user.user_id,
                                  'id': user.id,
                                  'first_name':user.first_name,
                                  'last_name':user.last_name,
                                  'email':user.email,
                                  'phone':user.phone,
                                  'sex':user.sex,
                                  'status':user.status,
                                  'created_at':user.created_at,
                                  'updated_at':user.updated_at
                                   },
                                  'record_info':{
                                      'page': page,
                                      'per_page': per_page,
                                      'total_pages': total_pages,
                                      'total_user': len(users)
                                  }

                }
        )

        # pagination implementation
        if page > 1:
            view_page = (page - 1) * per_page
            return jsonify(users=user_list[view_page:])
        view_page = page * per_page
        return jsonify(users=user_list[:view_page])
    else:
        return jsonify(Response={'error':f'No user found with id {country_id}'})


@app.route('/<int:user_id>/user')
def get_user(user_id):
    user = Users.query.get(user_id)
    if user:
            if user.status:
                return jsonify(user={
                                        'country_id': user.country_id,
                                        'uuid': user.user_id,
                                        'first_name': user.first_name,
                                        'last_name': user.last_name,
                                        'id': user.id,
                                        'email': user.email,
                                        'phone': user.phone,
                                        'sex': user.sex,
                                        'status': user.status,
                                        'created_at': user.created_at,
                                        'updated_at': user.updated_at
                                      }
                                 )
    return jsonify(Response={'error':f'No user found with id {user_id}'})


@app.route('/<int:user_id>/update_user', methods=['PATCH'])
def update_user(user_id):
    user = Users.query.get(user_id)
    if user.status:
        user.first_name = request.form.get('firstname')
        user.last_name = request.form.get('lastname')
        user_country = request.form.get('country')
        user.country_id = db.session.query(Countries).filter_by(country_name=user_country).first().id
        user.sex = request.form.get('sex')
        user.updated_at = datetime.datetime.now()

        db.session.commit()
        return jsonify(Response={'Success':'User information successfully updated'})
    return jsonify(Response={'error': f'No user found with id {user_id}'})



@app.route('/<int:user_id>/delete_user', methods=['DELETE'])
def delete_user(user_id):
    user = Users.query.get(user_id)
    if user:
        db.session.delete(user)
        db.session.commit()
        return jsonify(Response={'Success': 'Successfully deleted'})
    return jsonify(Response={'error': f'No user found with id {user_id}'})


@app.route('/<int:user_id>/activate_user', methods=['PATCH'])
def activate_user(user_id):
    user = Users.query.get(user_id)
    if user:
        user.status = True
        user.updated_at = datetime.datetime.now()
        db.session.commit()
        return jsonify(Response={'Success': 'User successfully activated'})
    return jsonify(Response={'error': f'No user found with id {user_id}'})


@app.route('/<int:user_id>/deactivate_user', methods=['PATCH'])
def deactivate_user(user_id):
    user = Users.query.get(user_id)
    if user:
        user.status = False
        user.updated_at = datetime.datetime.utcnow()
        db.session.commit()
        return jsonify(Response={'Success': 'User successfully deactivated'})
    return jsonify(Response={'error': f'No user found with id {user_id}'})


@app.route('/all_countries')
def get_all_countries():
    countries = db.session.query(Countries).all()

    country_list = []
    for country in countries:
        country_list.append({
                             'country_name': country.country_name,
                              'country_code':country.country_code,
                              'short_code': country.short_code
                              }
                            )

    return jsonify(Countries=country_list)


if __name__ == '__main__':
    app.run(debug=True)
