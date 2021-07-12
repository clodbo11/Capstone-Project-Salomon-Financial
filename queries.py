from app import db
from models import Stock_holding, User, Stock_holding, Transaction
from sqlalchemy.sql import func



def insert_stock(symbol, name, quantity):
    """ Add a new stock to the database """
    stock = Stock_holding(symbol=symbol, name=name, quantity=quantity)
    db.session.add(stock)
    db.session.commit()

def insert_transaction(user_id, stock_id, quantity, price, type):
    """ Add a new transaction (buy or sell) """
    transaction = Transaction(user_id=user_id, stock_id=stock_id,
            quantity=quantity, price=price, type=type)
    db.session.add(transaction)
    db.session.commit()

def insert_user(username, password):
    """Create new user"""
    new_user = User(username=username, password=password)
    db.session.add(new_user)
    db.session.commit()

def select_all_users():
    """Get all users"""
    return User.query.all()

def select_user_by_id(user_id):
    """Get user object where id"""
    return User.query.filter_by(id=user_id).first()

def select_user_by_username(username):
    """Get user object where username"""
    return User.query.filter_by(username=username).first()

def select_stock_by_symbol(symbol):
    """Get stock object where symbol"""
    return Stock_holding.query.filter_by(symbol=symbol).first()

def select_stocks_by_user(user_id):
    """Get list of stocks owned by a given user"""
    return (db.session.query(
                func.sum(Transaction.quantity).label('quantity'),
                Stock_holding.name,
                Stock_holding.symbol,
                Stock_holding.quantity
            ).join(User).join(Stock_holding).group_by(
                Transaction.stock_id, Stock_holding, User
            ).filter(User.id==user_id).all())

def select_transactions_by_user(user_id):
    """Get a list of all a user's transactions"""
    return (db.session.query(
                Transaction.id,
                Transaction.quantity,
                Transaction.price,
                Transaction.time,
                Transaction.type,
                Stock_holding.name,
                Stock_holding.symbol,
            ).join(Stock_holding).filter(
                Transaction.user_id==user_id
            ).all())


def select_transactions_by_stock(stock_id, user_id):
    """Get the sum of all a user's transactions of a certain stock"""
    return (db.session.query(
                func.sum(Transaction.quantity).label('shares')
            ).group_by(
                Transaction.stock_id
            ).filter(
                Transaction.stock_id == stock_id,
                Transaction.user_id == user_id
            ).one())

def update_user_cash(change, user_id):
    """ Change user cash after buy or sell """
    user = select_user_by_id(user_id)
    user.cash = user.cash + change
    db.session.commit()

def update_user_share(change, symbol):
    """Change user's number of shares after buy or sell"""
    stock=select_stock_by_symbol(symbol)
    stock.quantity=stock.quantity-change
    db.session.commit()

def update_user_hash(new_hash, user_id):
    """ Update the user's password hash on password reset """
    user = select_user_by_id(user_id)
    user.password_hash = new_hash
    db.session.commit()