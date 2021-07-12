from datetime import datetime

from flask_bcrypt import Bcrypt
from flask_sqlalchemy import SQLAlchemy



db = SQLAlchemy()

def connect_db(app):
    """Connect to database."""

    db.app = app
    db.init_app(app)

class User(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String, unique=True, nullable=False)
    password = db.Column(db.Text, nullable=False)
    cash = db.Column(db.Float, default=500000.00)
    transactions = db.relationship('Transaction', cascade='all,delete',
            backref='user')

    def __repr__(self):
        return f'<User {self.username}>'


class Stock_holding(db.Model):
    __tablename__ = 'stock_holding'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    symbol = db.Column(db.String(20), unique=False, nullable=False)
    quantity=db.Column(db.Integer, nullable=False)
    name = db.Column(db.String(80), unique=False, nullable=False)
    transactions = db.relationship('Transaction', cascade='all,delete',
            backref='stock')

    def __repr__(self):
        return f'<Stock {self.symbol}>'


class Transaction(db.Model):
    __tablename__ = 'transaction'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    user_id = db.Column(db.Integer,
        db.ForeignKey('users.id', ondelete='CASCADE'),
        nullable=False)

    stock_id = db.Column(db.Integer,
        db.ForeignKey('stock_holding.id', ondelete='CASCADE'),
        nullable=False)

    quantity = db.Column(db.Float, nullable=False)
    price = db.Column(db.Float, nullable=False)
    type = db.Column(db.String, nullable=False)
    time = db.Column(db.DateTime, nullable=False,
        default=datetime.now(tz=None))

    def __repr__(self):
        return f'<Transaction {self.user}: {self.stock_holding}>'