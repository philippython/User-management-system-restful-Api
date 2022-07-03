from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import uuid
from sqlalchemy import Column, ForeignKey, Integer, String, DateTime, Boolean, Text
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func

app = Flask(__name__)


app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///UserManagement.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# creating all database tables


class Countries(db.Model):
    id = Column(Integer, primary_key=True, unique=True)
    country_code = Column(String(80), unique=True, nullable=False)
    country_name = Column(String(120), unique=True, nullable=False)
    short_code = Column(String(80), unique=True, nullable=False)

    users = relationship('Users', backref='user')


class Users(db.Model):
    id = Column(Integer, primary_key=True, unique=True)
    user_id = Column('id', Text(length=36), default=lambda: str(uuid.uuid4()), primary_key=True)  # uuid field
    first_name = Column(String(80), unique=True, nullable=False)
    last_name = Column(String(120), unique=True, nullable=False)
    email = Column(String(80), unique=True, nullable=False)
    phone = Column(String(80), unique=True, nullable=False)
    sex = Column(String(80), unique=True, nullable=False)
    status = Column(Boolean, unique=True, nullable=False)
    created_at = Column(DateTime(timezone=True), server_default=func.now()) # current time of creation
    updated_at = Column(DateTime(timezone=True), onupdate=func.now()) # time of update(i.e patch request)
    country_id = Column(Integer, ForeignKey('countries.id'))


db.create_all()


if __name__ == '__main__':
    app.run(debug=True)
